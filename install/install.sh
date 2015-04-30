#!/bin/bash

# Copyright (C) 2014 CDR-port
# cdr-port@cdr-port.net

# Configurar o Branch
BRANCH='devel'

apt-get update -y
apt-get upgrade -y
apt-get -y install lsb-release gawk

#Instala o menu
cd /usr/src/
wget --no-check-certificate  https://raw.githubusercontent.com/eluizbr/cdr-port/$BRANCH/install/funcoes.sh
wget --no-check-certificate  https://raw.githubusercontent.com/eluizbr/cdr-port/$BRANCH/install/menu.sh
bash menu.sh

