#!/bin/bash

# Copyright (C) 2014 CDR-port
# cdr-port@cdr-port.net

# Config Global
USER_BANCO_MASTER='root'
SENHA_BANCO_MASTER='app2004'
USUARIO="$1_`</dev/urandom tr -dc A-Za-z0-9| (head -c $1 > /dev/null 2>&1 || head -c 5)`"
IFCONFIG=`which ifconfig 2>/dev/null||echo /sbin/ifconfig`
IPADDR=`$IFCONFIG eth0|gawk '/inet addr/{print $2}'|gawk -F: '{print $2}'`
IP='177.52.104.53'
INSTALL_DIR="/usr/share/cdrport/$USUARIO"
CONFIG_DIR="/usr/share/cdrport/$USUARIO/cdr-port"
BRANCH='master'
NOME_BANCO="$1_`</dev/urandom tr -dc A-Za-z0-9| (head -c $1 > /dev/null 2>&1 || head -c 10)`"
USER_BANCO="$1_`</dev/urandom tr -dc A-Za-z0-9| (head -c $1 > /dev/null 2>&1 || head -c 5)`"
SENHA_BANCO=`</dev/urandom tr -dc A-Za-z0-9| (head -c $1 > /dev/null 2>&1 || head -c 20)`
echo "$SENHA_BANCO" / "$NOME_BANCO"  > /usr/src/mysql_"$USER_BANCO".txt

# VARIAVEIS NAO MUTAVEIS

uri='$uri'
proxy_add_x_forwarded_for='$proxy_add_x_forwarded_for'
http_host='$http_host'
LOGFILE='$LOGFILE'
LOGDIR='$(dirname $LOGFILE)'
LOGDIR_1='$LOGDIR'
NUM_WORKERS='$NUM_WORKERS'
USER='$USER'
GROUP='$GROUP'


#Instalando MySQL
#clear
echo $USER_BANCO_MASTER / $SENHA_BANCO_MASTER
mysql -u "$USER_BANCO_MASTER" -p"$SENHA_BANCO_MASTER" -e "CREATE DATABASE $NOME_BANCO"
mysql -u "$USER_BANCO_MASTER" -p"$SENHA_BANCO_MASTER" -e "CREATE USER '$USER_BANCO'@'localhost' IDENTIFIED BY '$SENHA_BANCO';"
mysql -u "$USER_BANCO_MASTER" -p"$SENHA_BANCO_MASTER" -e "GRANT ALL PRIVILEGES ON $NOME_BANCO.* TO '$USER_BANCO'@'localhost' with grant option;"
mysql -u "$USER_BANCO_MASTER" -p"$SENHA_BANCO_MASTER" -e "FLUSH PRIVILEGES;"

#Instalando CDR-port
#clear
mkdir -p $INSTALL_DIR
cd $INSTALL_DIR
git clone -b $BRANCH https://github.com/eluizbr/cdr-port.git
virtualenv  --system-site-packages cdr-port
cd cdr-port

source bin/activate
pip install -r $CONFIG_DIR/install/conf/requirements.txt


sed -i "s/NOME_BANCO/$NOME_BANCO/" $CONFIG_DIR/install/conf/settings_base.txt
sed -i "s/USER_BANCO/$USER_BANCO/" $CONFIG_DIR/install/conf/settings_base.txt
sed -i "s/SENHA_BANCO/$SENHA_BANCO/" $CONFIG_DIR/install/conf/settings_base.txt

cp $CONFIG_DIR/install/conf/settings_base.txt $CONFIG_DIR/cdrport/settings.py

rm -rf $CONFIG_DIR/cdr-port/*/migrations
rm -rf cdr/migrations

python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'app2004')" | ./manage.py shell
python manage.py collectstatic --noinput

wget -c https://github.com/eluizbr/cdr-port/raw/master/install/sql/base.sql.zip -O install/sql/base.sql.zip
unzip $CONFIG_DIR/install/sql/base.sql.zip  -d $CONFIG_DIR/install/sql/
mysql -u "$USER_BANCO_MASTER" -p"$SENHA_BANCO_MASTER" "$NOME_BANCO" < $CONFIG_DIR/install/sql/base.sql
mysql -u "$USER_BANCO_MASTER" -p"$SENHA_BANCO_MASTER" "$NOME_BANCO" < $CONFIG_DIR/install/sql/rotinas.sql
mysql -u "$USER_BANCO_MASTER" -p"$SENHA_BANCO_MASTER" "$NOME_BANCO" < $CONFIG_DIR/install/sql/views.sql
mysql -u "$USER_BANCO_MASTER" -p"$SENHA_BANCO_MASTER" "$NOME_BANCO" < $CONFIG_DIR/install/sql/portados.sql
mysql -u "$USER_BANCO_MASTER" -p"$SENHA_BANCO_MASTER" "$NOME_BANCO" < $CONFIG_DIR/install/sql/ramal.sql
mysql -u "$USER_BANCO_MASTER" -p"$SENHA_BANCO_MASTER" "$NOME_BANCO" < $CONFIG_DIR/install/sql/info.sql
mysql -u "$USER_BANCO_MASTER" -p"$SENHA_BANCO_MASTER" "$NOME_BANCO" < $CONFIG_DIR/install/sql/tmp_canais.sql
mysql -u "$USER_BANCO_MASTER" -p"$SENHA_BANCO_MASTER" "$NOME_BANCO" -e "ALTER TABLE cdr_cdr ALTER COLUMN portado SET DEFAULT 'Nao';"
#sed -i "s/SENHA_DB/$SENHA_BANCO/" $CONFIG_DIR/install/valida.py
#python $CONFIG_DIR/install/valida.py
rm -rf $CONFIG_DIR/install/sql/base.sql.zip

python cloudflare.py $USUARIO 2a8cae54633ca66626731e28871cb65553fe3 create

echo "
    $IP     $USUARIO.cdr-port.net   $USUARIO
" >> /etc/hosts


### Config nginx

echo "upstream cdrport_server {
        #server unix:/tmp/gunicorn.sock fail_timeout=0;
        # For a TCP configuration:
        server $IPADDR:8000 fail_timeout=0;
    }

server {
        #listen 80 default;
        client_max_body_size 4G;
        server_name $USUARIO.cdr-port.net;

        keepalive_timeout 5;

        # path for static files

    location /static/ {
        alias $CONFIG_DIR/cdr/static/;
        expires 30d;
    }
    
    location /gravacao/ {
        alias /var/spool/asterisk/monitor/;
        expires 30d;
    autoindex on;
    }

        location / {
            # checks for static file, if not found proxy to app
            try_files $uri @proxy_to_app;
        }
location @proxy_to_app {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_redirect off;

            proxy_pass   http://cdrport_server;
        }

}" > /etc/nginx/sites-enabled/cdrport_"$USER_BANCO".conf
/etc/init.d/nginx reload

### FIM Config nginx

#cp $CONFIG_DIR/install/conf/my.cnf /etc/mysql/
#/etc/init.d/mysql restart

### INICIO arquivo incialização

echo "#!/bin/bash
set -e
LOGFILE=/var/log/cdrport/$USER_BANCO/gunicorn_cdrport.log
LOGDIR=$LOGDIR

# The number of workers is number of worker processes that will serve requests.
# You can set it as low as 1 if you’re on a small VPS.
# A popular formula is 1 + 2 * number_of_cpus on the machine (the logic being,
# half of the processess will be waiting for I/O, such as database).
NUM_WORKERS=1

# user/group to run as
USER=www-data
GROUP=www-data

cd $CONFIG_DIR
source bin/activate

test -d $LOGDIR_1 || mkdir -p $LOGDIR_1

#Execute unicorn
exec gunicorn cdrport.wsgi:application -b 0.0.0.0:8000 -w $NUM_WORKERS --timeout=300 \
    --user=$USER --group=$GROUP --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE -D" > /etc/init.d/cdrport_"$USER_BANCO".sh


cd $INSTALL_DIR
chown -R www-data cdr-port
chmod +x /etc/init.d/cdrport_"$USER_BANCO".sh
/etc/init.d/cdrport_"$USER_BANCO".sh
echo "/etc/init.d/cdrport_$USER_BANCO.sh" >> /etc/rc.local
### FIM arquivo incialização
deactivate
ExitFinish=1

