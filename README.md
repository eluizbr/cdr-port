Bem-Vindo ao CDR-port
=====================


***CDR-port*** é uma apliacação desenvolvida em Python utilizando o Framework
[Django](https://www.djangoproject.com/), que tem como objetivo, criar uma interface CDR (Call Detail Reports) 
para [Asterisk](http://www.asterisk.org/) nas versões 1.8.X, 10.X, 11.X, 12.X .


Compatibilidade
---------------

O ***CDR-port***, é compativel com todas as versões do [Asterisk](http://www.asterisk.org/) => 1.8.X, 10.X, 11.X, 12.X .
O [Asterisk](http://www.asterisk.org/) deve ser compilado com suporte a MySQL.

Diferenças entre versões
------------------------

O ***CDR-port*** tem 2 versões:

- PREMIUM - Esta versão traz como grande diferencial, o sistema de portabilidade e a base de portabilidade LOCAL instalada 
em seu servidor. [Valores das versões](http://www.cdr-port.net/pricing-table.html)

- FREE -  Esta versão possuiu todos os recursos da versão PREMIUM, com exceção da base de portabilidade. Se você já tiver uma
base de portabilidade, é possível instalar ela na versão FREE e a converter para versão PREMIUM.

    - O ***CDR-port*** não suporta consultas on-line.


Instalação
-------------


***CDR-port*** é uma aplicação baseada em Django, será necessário instalar as seguintes dependências:


- [Python](https://www.python.org/) = 2.7.6 (Não testado em Python 3.X)
- [Django Framework](https://www.djangoproject.com/) = 1.7.5 (não foi testado em outras versões)
- [Nginx](http://nginx.com/solutions/web-server/)
- [Asterisk](http://www.asterisk.org/) => 1.8.X
- [MySQL](http://dev.mysql.com/downloads/) => 5.5.X
- [Ubuntu](http://www.ubuntu.com/download/server) => 12.04 LTS Server

    - Outras distribuições Linux são completamente compatíveis, basta você fazer
	as atapdacões necessárias no script de instalação.


O script de instalação, faz todo o processo necessário para instalar de forma automatizada o ***CDR-port***.
Tudo que você precisa fazer, é baixar e executar o script.

### Instalando o [Asterisk](http://www.asterisk.org/)

Para a instalação do [Asterisk](http://www.asterisk.org/), iremos adotar os seguintes componentes:

* [Ubuntu](http://www.ubuntu.com/server) => 12.04 LTS Server
* [Asterisk](http://www.asterisk.org/) 1.8.28.2

#### Instalando e compilando o [Asterisk](http://www.asterisk.org/):

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

### Instalando o ***CDR-port***

#### Script de instalação


Temos um script para instalação automatizada do ***CDR-port***. 

```
cd /usr/src/
wget https://github.com/eluizbr/cdr-port/raw/master/install/install.sh
bash install.sh
```

Ao executar o processo acima, toda a instalação é realizada de forma automatizada. Ao final do processo, você poderá acessar
o ***CDR-port***.

```
	http:\\IP-DO_SERVIDOR
```

Outro ponto importante, é a senha do MySQL, ela é gerada de forma randômica durante a instalação. O script grava essa senha em
um arquivo para consulta posterior.

```
cat /usr/src/mysql_senha.txt
```

* Se você já possue uma instalação do MySQL, você deverá alterar no script de instalação o parametro `DB_PASSWORD` no incio do script 
para `DB_PASSWORD=SUA_SENHA` .


#### Configurando o ***CDR-port***

Você deve configurar sua localidade no ***CDR-port*** acessando a seguinte url:


```
    http:\\IP-DO_SERVIDOR/admin/cdr/
```

*Você irá precisar do usuário e senha criados durante a instalação do ***CDR-port***.

Configure seu DDD, Estado, Cidade, Cortar (digitos a serem cortados. Ex: Se você disca 551120304050, você deve cortar o 55, digitando 2 para cortar os 2 primeiros digitos.), Audio (Se você grava ligações, escolha SIM) e suas tarifas. Essas configurações são fundamentais para o funcionamento correto do ***CDR-port***.



### Configurando o [Asterisk](http://www.asterisk.org/) para o ***CDR-port***

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
userfield=1

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

### Usando o ***CDR-port***


Se você estiver usando a portabilidade, você devereá encaminhar as chamadas sem "ZERO", exemplo:

```
30405060 (LOCAL 8 digitos)
1130405060 (LDN 10 digitos)
230405060 (LOCAL 9 digitos)
11230405060 (LDN 11 digitos)
```

Se você tem necessidade de enviar chamadas da forma diferente da referenciada acima, você deverá tratar a chamada antes de chegar ao ***CDR-port*** .


Status atual
------------


#### CDR para [Asterisk](http://www.asterisk.org/)
===================================================

Legenda:
>
- [X] Pronto para o uso
- [ ] Em desenvolvimento

##### Setup

- [X] Setup automatizado
- [X] Integração descomplicada
	- Edite apenas um arquivo para integrar o ***CDR-port*** ao [Asterisk](http://www.asterisk.org/) (cdr_mysql.conf)

##### Integração

- [X] Integração com [Asterisk](http://www.asterisk.org/)

##### Dashboard

- [ ] Mapa
- [X] Estatisticas de chamadas
- [X] Últimos números atendidos
- [X] Ligações por operadora
- [X] Calendário ligações diárias

##### CDR

- [X] Estatisticas (Atendidas, Não atendidas, Ocupadas, Número não existe)
- [X] Pesquisa por ramal
- [X] Pesquisa por número
- [X] Por status (Atendidas, Não atendidas, Ocupadas, Número não existe)
- [X] Por cidade
- [X] Por estado
- [X] Por range de data
- [X] Arquivos de gravação de áudio

##### Billing

- [X] Tarifação
    - [ ] Configuração de cadências

- [X] Configuração de custo (FIXO-Local, FIXO-LDN, Móvel-Local, Móvel-LDN)
    - [ ] Rotas DDI

#### Portabilidade
==================
	
##### Integração

- [ ] Integração com [Asterisk](http://www.asterisk.org/)
- [X] Integração descomplicada com o extensions.conf

```
10 Digitos
exten => _XXXXXXXXXX,1,Answer()
exten => _XXXXXXXXXX,n,AGI(/root/cdrport.py,${EXTEN})
exten => _XXXXXXXXXX,n,NoOp(${NUMERO})
exten => _XXXXXXXXXX,n,Dial(SIP/${NUMERO})
exten => _XXXXXXXXXX,n,Dial(SIP/OPERADORA/0${NUMERO:3})
exten => _XXXXXXXXXX,n,Hangup

11 Digitos
exten => _XXXXXXXXXXX,1,Answer()
exten => _XXXXXXXXXXX,n,AGI(/root/cdrport.py,${EXTEN})
exten => _XXXXXXXXXXX,n,NoOp(${NUMERO})
exten => _XXXXXXXXXXX,n,Dial(SIP/${NUMERO})
exten => _XXXXXXXXXXX,n,Dial(SIP/OPERADORA/0${NUMERO:3})
exten => _XXXXXXXXXXX,n,Hangup
```

##### CDR

- [X] Estatisticas por ramal
- [X] Estatisticas de portabilidade
- [X] Por CSP
- [X] Por Operadora
- [X] Por tipo ( Fixo, Móvel, Rádio)
- [X] Portabilidade ( Portado ou não portado)
- [X] Por cidade
- [X] Por estado
- [X] Por range de data
- [X] Arquivos de gravação de áudio

#### Billing
============

- [X] Tarifação
    - [ ] Configuração de cadências

- [X] Configuração de custo (FIXO-Local, FIXO-LDN, Móvel-Local, Móvel-LDN)
    - [ ] Rotas DDI

### PABX
=========

- [ ] Estatisticas do Asterisk
- [ ] Ramais
    - [ ] Editar 
    - [ ] Criar 
    - [ ] Visualizar 
    - [ ] Status
- [ ] Extensions
    - [ ] Editar 
    - [ ] Criar 
    - [ ] Visualizar 
    - [ ] Status
- [ ] Filas
    - [ ] Editar 
    - [ ] Criar 
    - [ ] Visualizar 
    - [ ] Status
- [ ] IRV
    - [ ] Editar 
    - [ ] Criar 
    - [ ] Visualizar 
    - [ ] Status

Suporte
--------

Para suporte acesse :

[suporte](https://github.com/eluizbr/cdr-port/issues)	


Screenshot
----------

* Dashboard :


![Dashboard]
(https://github.com/cdr-port/cdr-port.github.io/raw/master/img/dashboard.png)


* Dashboard - Resumos :


![Dashboard Resumos]
(https://github.com/cdr-port/cdr-port.github.io/raw/master/img/dashboar-2.png)


* CDR Versão BÁSICO :


![CDR]
(https://github.com/cdr-port/cdr-port.github.io/raw/master/img/cdr-3.png)


* CDR Versão com PORTABILIDADE :

![CDR PREMIUM]
(https://github.com/cdr-port/cdr-port.github.io/raw/master/img/cdr-4.png)


* CDR -  Gravação:

![ÁUDIO]
(https://github.com/cdr-port/cdr-port.github.io/raw/master/img/audio.png)

