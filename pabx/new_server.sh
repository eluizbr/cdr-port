#!/bin/bash

# Copyright (C) 2014 CDR-port
# cdr-port@cdr-port.net

# Config Global
USUARIO="$1"
IFCONFIG=`which ifconfig 2>/dev/null||echo /sbin/ifconfig`
IPADDR=`$IFCONFIG eth0|gawk '/inet addr/{print $2}'|gawk -F: '{print $2}'`
INSTALL_DIR="/usr/share/cdrport/$USUARIO"
CONFIG_DIR="/usr/share/cdrport/$USUARIO/cdr-port"
BRANCH='devel'
NOME_BANCO="$1-`</dev/urandom tr -dc A-Za-z0-9| (head -c $1 > /dev/null 2>&1 || head -c 10)`"
USER_BANCO="$1-`</dev/urandom tr -dc A-Za-z0-9| (head -c $1 > /dev/null 2>&1 || head -c 10)`" 
SENHA_BANCO=`</dev/urandom tr -dc A-Za-z0-9| (head -c $1 > /dev/null 2>&1 || head -c 20)`
echo "$SENHA_BANCO" > /usr/src/mysql_"$USER_BANCO".txt
echo $1

#Instalando CDR-port
mkdir -p $INSTALL_DIR
cd $INSTALL_DIR


#Instalando CDR-port
clear
mkdir -p $INSTALL_DIR
cd $INSTALL_DIR
git clone -b $BRANCH https://github.com/eluizbr/cdr-port.git
virtualenv --system-site-packages cdr-port
cd cdr-port
pip install -r $CONFIG_DIR/install/conf/requirements.txt
sed -i "s/NOME_BANCO/$NOME_BANCO/" $CONFIG_DIR/install/conf/settings.txt
sed -i "s/USER_BANCO/$USER_BANCO/" $CONFIG_DIR/install/conf/settings.txt
sed -i "s/SENHA_BANCO/$SENHA_BANCO/" $CONFIG_DIR/install/conf/settings.txt
cp $CONFIG_DIR/install/conf/settings.txt /usr/share/cdrport/cdr-port/cdrport/settings.py
rm -rf $CONFIG_DIR/cdr-port/*/migrations
python manage.py syncdb
python manage.py collectstatic --noinput

wget -c https://github.com/eluizbr/cdr-port/raw/master/install/sql/base.sql.zip -O install/sql/base.sql.zip
unzip $CONFIG_DIR/install/sql/base.sql.zip  -d $CONFIG_DIR/install/sql/
mysql -u "$USER_BANCO" -p"$SENHA_BANCO" "$NOME_BANCO" < $CONFIG_DIR/install/sql/base.sql
mysql -u "$USER_BANCO" -p"$SENHA_BANCO" "$NOME_BANCO" < $CONFIG_DIR/install/sql/rotinas.sql
mysql -u "$USER_BANCO" -p"$SENHA_BANCO" "$NOME_BANCO" < $CONFIG_DIR/install/sql/views.sql
mysql -u "$USER_BANCO" -p"$SENHA_BANCO" "$NOME_BANCO" < $CONFIG_DIR/install/sql/portados.sql
mysql -u "$USER_BANCO" -p"$SENHA_BANCO" "$NOME_BANCO" < $CONFIG_DIR/install/sql/ramal.sql
mysql -u "$USER_BANCO" -p"$SENHA_BANCO" "$NOME_BANCO" < $CONFIG_DIR/install/sql/tmp_canais.sql
mysql -u "$USER_BANCO" -p"$SENHA_BANCO" "$NOME_BANCO" -e "ALTER TABLE cdr_cdr ALTER COLUMN portado SET DEFAULT 'Nao';"
sed -i "s/SENHA_DB/$SENHA_BANCO/" $CONFIG_DIR/install/valida.py
#python $CONFIG_DIR/install/valida.py
rm -rf $CONFIG_DIR/install/sql/base.sql.zip

### Config nginx

cat $CONFIG_DIR/install/conf/cdrport_nginx_base.conf > /tmp/cdrport_"$USER_BANCO".conf


sed -i "s/127.0.0.1/$IPADDR/" /tmp/cdrport_"$USER_BANCO".conf
sed -i "s/CONFIG_DIR/$CONFIG_DIR/cdr/static/" /tmp/cdrport_"$USER_BANCO".conf

/etc/init.d/nginx reload

### FIM Config nginx

cp $CONFIG_DIR/install/conf/my.cnf /etc/mysql/
/etc/init.d/mysql restart

### INICIO arquivo incialização
cat $CONFIG_DIR/install/conf/cdrport_base.sh > /tmp/cdrport_"$USER_BANCO".sh

sed -i "s/INSTALL_DIR/$INSTALL_DIR/" /tmp/cdrport_"$USER_BANCO".sh
sed -i "s/USER_BANCO/$USER_BANCO/" /tmp/cdrport_"$USER_BANCO".sh
chmod +x /tmp/cdrport_"$USER_BANCO".sh
mv /tmp/cdrport_"$USER_BANCO".sh /etc/init.d/
cd $INSTALL_DIR
chown -R www-data cdr-port
/etc/init.d/cdrport_"$USER_BANCO".sh
echo "/etc/init.d/cdrport_'$USER_BANCO'.sh" >> /etc/rc.local
### FIM arquivo incialização

ExitFinish=1


