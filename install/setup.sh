#!/bin/bash

# Copyright (C) 2014 CDR-port
# cdr-port@cdr-port.net


apt-get -y update
apt-get -y upgrade
apt-get remove ajenti -y
apt-get install build-essential  -y
apt-get install python-virtualenv python-mysqldb python-dev python-imaging unzip git -y
apt-get install nginx -y

export DEBIAN_FRONTEND=noninteractive
apt-get install -q -y mysql-server mysql-client libmysqlclient-dev -y
mysqladmin -u root password app2004
mysql -u root -papp2004 -e "create database portabilidade";

cd /usr/src/
git clone https://github.com/rdegges/pyst2.git
cd pyst2
python setup.py install --prefix=/usr/local
rm -rf pyst2
cd /usr/src/

mkdir -p /usr/src/deploy/virtualenvs
cd /usr/src/deploy/virtualenvs
git clone https://github.com/cdr-port/cdr-port.git
virtualenv --system-site-packages cdr-port
cd cdr-port
pip install -r requirements.txt


cp -rf install/settings.py portabilidade/ 

chmod +x manage.py
python manage.py syncdb
python manage.py collectstatic

pip install gunicorn
cp install/portabilidade_nginx.conf /etc/nginx/sites-enabled/portabilidade

cp install/memoria.sh /etc/cron.hourly/
chmod +x /etc/cron.hourly/memoria.sh
bash /etc/cron.hourly/memoria.sh

cd install

unzip base.sql.zip
mysql -u root -papp2004 portabilidade < base.sql
mysql -u root -papp2004 portabilidade < config_operadora.sql
mysql -u root -papp2004 portabilidade < views.sql
mysql -u root -papp2004 portabilidade < rotinas.sql
mysql -u root -papp2004 portabilidade -e "SET GLOBAL binlog_format = 'ROW';"
mysql -u root -papp2004 portabilidade -e  "grant all on *.* to 'root'@'%' identified by 'app2004' with grant option;"
#mysql -u root -papp2004 portabilidade -e "UPDATE nao_portados  SET operadora = 'VIVO' WHERE operadora = 'TELEFONICA'"
#mysql -u root -papp2004 portabilidade -e "UPDATE nao_portados  SET tipo = 'MOVEL' WHERE tipo = 'MÓVEL'"
#mysql -u root -papp2004 portabilidade -e "UPDATE nao_portados  SET tipo = 'RADIO' WHERE tipo = 'RÁDIO'"

chmod +x gunicorn_launcher.sh
cp gunicorn_launcher.sh /etc/init.d/
update-rc.d  gunicorn_launcher.sh defaults
cp memoria.sh /etc/cron.hourly/
/etc/init.d/cron restart
cd /usr/src/
chown -R www-data deploy/

echo "/etc/init.d/gunicorn_launcher.sh start" >> /etc/rc.local
/etc/init.d/gunicorn_launcher.sh start


