#!/bin/bash

# Copyright (C) 2014 CDR-port
# cdr-port@cdr-port.net
apt-get install -y  build-essential linux-headers-`uname -r` make bison flex  zip  curl sox  lshw ncurses-term ttf-bitstream-vera libncurses5-dev automake libtool mpg123 sqlite3 libsqlite3-dev libncursesw5-dev uuid-dev  libxml2-dev libnewt-dev  pkg-config  autoconf subversion  libltdl-dev libltdl7 libcurl3   libxml2-dev   libiksemel-dev libssl-dev libnewt-dev libusb-dev libeditline-dev libedit-dev libssl-dev 
#Instalando ASTERISK
clear
rm -rf asterisk*
cd /usr/src/
wget -c http://downloads.asterisk.org/pub/telephony/asterisk/old-releases/asterisk-1.8.28.2.tar.gz
tar zxvf asterisk-1.8.28.2.tar.gz
ln -s asterisk-1.8.28.2 asterisk
cd asterisk
make distclean
./configure
contrib/scripts/get_mp3_source.sh
make menuselect.makeopts
menuselect/menuselect --disable CORE-SOUNDS-EN-GSM --enable app_mysql --enable cdr_mysql --enable res_config_mysql --enable cdr_odbc --enable res_odbc --enable res_config_odbc --enable  format_mp3 --enable cdr_csv menuselect.makeopts
make
make install
make config
make samples
ldconfig
cd ..
/etc/init.d/asterisk restart
echo done
