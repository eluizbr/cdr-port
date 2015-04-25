Bem-Vindo a documentação do CDR-port!
=====================================



CDR-port é uma apliacação desenvolvida em Python utilizando o Framework
Django, que tem como objetivo, criar uma interface CDR (Call Detail Reports) 
para Asterisk nas versões 1.8.X, 10.X, 11.X, 12.X .


Quem deve utilizar?
-------------------

Toda e qualquer empresa e ou profissionais que desejam ter sistema de relátorios
para telefonia objetivo.


Compatibilidade
---------------

O CDR-port, é compativel com todas as versões do Asterisk => 1.8.X, 10.X, 11.X, 12.X .
O Asterisk deve ser compilado com suporte a MySQL.


# Instalação


CDR-port é uma aplicação baseada em Django, e para a versão FRRE, 
será necessário instalar as seguintes dependências:


    - python >= 2.6
    - Django Framework = 1.7.5 (não foi testado em outras versões)
    - Nginx


Todas as dependências podem ser facilmente instaladas usando o PIP:

    - https://github.com/cdr-port/cdr-port/blob/master/install/requirements.txt


O script de instalação, faz todo o processo necessário para instalar de forma automadizada o CDR-port.
Tudo que você precisa fazer, é baixar e executar o script.

### Instalando o asterisk

Para a instalação do Asterisk, iremos adotar os seguintes componentes:

* Ubuntu 12.04 LTS Server
* Asterisk 1.8.28.2

#### Instalando e copilando o asterisk:

##### Dependências:

```
apt-get update -y
apt-get upgrade -y
apt-get install -y  build-essential linux-headers-`uname -r` make bison flex  zip  curl sox 
lshw ncurses-term ttf-bitstream-vera libncurses5-dev automake libtool mpg123 sqlite3 libsqlite3-dev 
libncursesw5-dev uuid-dev  libxml2-dev libnewt-dev  pkg-config  autoconf subversion  
libltdl-dev libltdl7 libcurl3   libxml2-dev   libiksemel-dev libssl-dev libnewt-dev libusb-dev 
libeditline-dev libedit-dev libssl-dev
```
##### Compliando:

```
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

```

### Instalando o CDR-port

#### Script de instalação


Temos um script para instalação automadizada do CDR-port. 

```
	cd /usr/src/
    wget https://github.com/cdr-port/cdr-port/raw/master/install/setup.sh
    bash setup.sh
```




Screenshot
----------

* Dashboard :


![Dashboard]
(https://github.com/eluizbr/cdr-port/raw/devel/cdr/img/dashborad.png)


* Dashboard - Resumos :


![Dashboard Resumos]
(https://github.com/eluizbr/cdr-port/raw/devel/cdr/img/dashboar-2.png)


* CDR Versão FREE :


![CDR]
(https://github.com/eluizbr/cdr-port/raw/devel/cdr/img/cdr-free.png)


* CDR Versão PREMIUM :

![CDR PREMIUM]
(https://github.com/eluizbr/cdr-port/raw/devel/cdr/img/cdr-premium-2.png)