#!/bin/bash

# Copyright (C) 2014 CDR-port
# cdr-port@cdr-port.net

# Configurar o Branch
BRANCH='devel'

apt-get -y install lsb-release

# Identify Linux Distribution type
func_identify_os() {
    if [ -f /etc/debian_version ] ; then
        DIST='UBUNTU12'
        
        if [ "$(lsb_release -cs)" != "trusty" ] ; then
            	echo "A instalação funciona apenas no Ubuntu => 12.04 LTS Server"
            	exit 255
        fi
        
elif [ -f /etc/debian_version ]; then
        DIST='UBUNTU14'
        
        if [ "$(lsb_release -cs)" != "precise" ] ; then
            	echo "A instalação funciona apenas no Ubuntu => 12.04 LTS Server"
            	exit 255
        fi
else
        echo "A instalação funciona apenas no Ubuntu => 12.04 LTS Server"
        exit 1
    fi
}

func_identify_os

case $DIST in
	'UBUNTU14')
	    apt-get -y update
		apt-get -y upgrade

	;;
	'UBUNTU12')
	    apt-get -y update
		apt-get -y upgrade
	;;
esac

#Instala o menu
cd /usr/src/
wget --no-check-certificate  https://raw.githubusercontent.com/eluizbr/cdr-port/$BRANCH/install/funcoes.sh
wget --no-check-certificate  https://raw.githubusercontent.com/eluizbr/cdr-port/$BRANCH/install/menu.sh
bash menu.sh

