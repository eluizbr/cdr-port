Bem-Vindo a documentação do CDR-port!
=====================================



CDR-port é uma apliacação desenvolvida em Python utilizando o Framework
[Django](https://www.djangoproject.com/), que tem como objetivo, criar uma interface CDR (Call Detail Reports) 
para [Asterisk](http://www.asterisk.org/) nas versões 1.8.X, 10.X, 11.X, 12.X .


Quem deve utilizar?
-------------------

Toda e qualquer empresa e ou profissional que desejam ter um sistema de relátorios
para [Asterisk](http://www.asterisk.org/) simples, bonito e eficiente.


Compatibilidade
---------------

O CDR-port, é compativel com todas as versões do [Asterisk](http://www.asterisk.org/) => 1.8.X, 10.X, 11.X, 12.X .
O [Asterisk](http://www.asterisk.org/) deve ser compilado com suporte a MySQL.


# Instalação


CDR-port é uma aplicação baseada em Django, e para a versão FRRE, 
será necessário instalar as seguintes dependências:


    - python >= 2.6
    - Django Framework = 1.7.5 (não foi testado em outras versões)
    - Nginx
    - [Asterisk] (http://www.asterisk.org/) => 1.8.X
    - MySQL
    - [Ubuntu](http://www.ubuntu.com/server) => 12.04 LTS Server

	* Instalação em outras distirbuições Linux são completamente compatíveis, basta você fazer
	as atapdacões necessárias no script de instalação.

Todas as dependências podem ser facilmente instaladas usando o PIP:

    - https://github.com/cdr-port/cdr-port/blob/master/install/requirements.txt


O script de instalação, faz todo o processo necessário para instalar de forma automadizada o CDR-port.
Tudo que você precisa fazer, é baixar e executar o script.

### Instalando o [Asterisk](http://www.asterisk.org/)

Para a instalação do [Asterisk](http://www.asterisk.org/), iremos adotar os seguintes componentes:

* [Ubuntu](http://www.ubuntu.com/server) => 12.04 LTS Server
* [Asterisk](http://www.asterisk.org/) 1.8.28.2

#### Instalando e copilando o [Asterisk](http://www.asterisk.org/):

##### Dependências:

```
apt-get update -y
apt-get upgrade -y
apt-get install -y  build-essential linux-headers-`uname -r` make bison flex  zip  curl sox 
lshw ncurses-term ttf-bitstream-vera libncurses5-dev automake libtool mpg123 sqlite3 
libsqlite3-dev libncursesw5-dev uuid-dev  libxml2-dev libnewt-dev  pkg-config  autoconf 
subversion libltdl-dev libltdl7 libcurl3   libxml2-dev   libiksemel-dev libssl-dev 
libnewt-dev libusb-dev libeditline-dev libedit-dev libssl-dev
```
##### Compliando:

* Você pode compilar o Asterisk a sua maneira, pode inclusive usar uma versão já instalada. A única regra aqui é
que precisamos do suporte ao MySQL.

```
clear
cd /usr/src/
wget -c http://downloads.asterisk.org/pub/telephony/asterisk/old-releases/asterisk-1.8.28.2.tar.gz
tar zxvf asterisk-1.8.28.2.tar.gz
ln -s asterisk-1.8.28.2 asterisk
cd asterisk
make distclean
./configure
contrib/scripts/get_mp3_source.sh
make menuselect.makeopts
menuselect/menuselect --disable CORE-SOUNDS-EN-GSM --enable app_mysql --enable cdr_mysql --enable res_config_mysql --enable format_mp3 menuselect.makeopts
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

* Ao executar o processo acima, toda a instalação é realizada de forma automadizada. Ao final do processo, você poderá acessar
o CDR-port.

```
	http:\\IP-DO_SERVIDOR
```
* Outro ponto importante, é a senha do MySQL, ela é gerada de forma randomica durante a instalação. O script grava essa senha em
um arquivo para consulta posterior.

```
cat /usr/src/mysql_senha.txt

```

* Caso você já possua uma instalação do MySQL, você deverá alterar no script de instalação o parametro `DB_PASSWORD` no incio do script 
para `DB_PASSWORD=SUA_SENHA` .


### Configurando o [Asterisk](http://www.asterisk.org/) para o CDR-port

A configuração do [Asterisk](http://www.asterisk.org/), se resume apenas ao arquivo `/etc/asterisk/cdr_mysql.conf`, que deve ter a configuração semelhante a 
demonstrada abaixo:

```
[global]
hostname=127.0.0.1
dbname=cdrport
table=cdr_cdr
password=SENHA_DB
user=root
port=3306

[columns]
alias start => calldate
alias clid => <a_field_not_named_clid>
alias src => <a_field_not_named_src>
alias dst => <a_field_not_named_dst>
alias dcontext => <a_field_not_named_dcontext>
alias channel => <a_field_not_named_channel>
alias dstchannel => <a_field_not_named_dstchannel>
alias lastapp => <a_field_not_named_lastapp>
alias lastdata => <a_field_not_named_lastdata>
alias duration => <a_field_not_named_duration>
alias billsec => <a_field_not_named_billsec>
alias disposition => <a_field_not_named_disposition>
alias amaflags => <a_field_not_named_amaflags>
alias accountcode => <a_field_not_named_accountcode>
alias userfield => <a_field_not_named_userfield>
alias uniqueid => <a_field_not_named_uniqueid>

```

Status atual
============

#### CDR para [Asterisk] (http://www.asterisk.org/)
===================================================

##### Setup

- [X] Setup automatizado
- [X] Integração descomplicada
	- Edite apenas um arquivo para integrar (cdr_mysql.conf)

##### Integração

- [X] Integração com [Asterisk](http://www.asterisk.org/)

##### CDR

- [X] Estatisticas de portabilidade
- [X] Estatisticas (Atendidas, Não atendidas, Ocupadas, Número não existe)
- [X] Pesquisa por ramal
- [X] Pesquisa por número
- [X] Por status (Atendidas, Não atendidas, Ocupadas, Número não existe)
- [X] Por cidade
- [X] Por estado
- [X] Por range de data

##### Billing

- [ ] Em desenvolvimento

#### Portabilidade
==================
	
##### Integração

- [ ] Integração com [Asterisk](http://www.asterisk.org/)
- [X] Integração descomplicada com o extensions.conf
	>
	``
	; 10 Digitos
	exten => _XXXXXXXXXX,1,Answer()
	exten => _XXXXXXXXXX,n,AGI(/root/executa.py,${EXTEN})
	exten => _XXXXXXXXXX,n,NoOp(${NUMERO})
	exten => _XXXXXXXXXX,n,Dial(SIP/${NUMERO})
	exten => _XXXXXXXXXX,n,Dial(SIP/GSM01/0${NUMERO:3})
	;exten => _XXXXXXXXXX,n,Goto(s-${DIALSTATUS},1)
	exten => _XXXXXXXXXX,n,Hangup

	; 11 Digitos
	exten => _XXXXXXXXXXX,1,Answer()
	exten => _XXXXXXXXXXX,n,AGI(/root/executa.py,${EXTEN})
	exten => _XXXXXXXXXXX,n,NoOp(${NUMERO})
	exten => _XXXXXXXXXXX,n,Dial(SIP/${NUMERO})
	exten => _XXXXXXXXXXX,n,Dial(SIP/GSM01/0${NUMERO:3})
	;exten => _XXXXXXXXXXX,n,Goto(s-${DIALSTATUS},1)
	exten => _XXXXXXXXXXX,n,Hangup
	``
	>

##### CDR

- [X] Por CSP
- [X] Por Operadora
- [X] Por tipo ( Portado ou não portado)
- [X] Por cidade
- [X] Por estado
- [X] Por range de data	

#### Billing
============

- [ ] Em desenvolvimento

- [ ] PABX
	* Em desenvolvimento


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