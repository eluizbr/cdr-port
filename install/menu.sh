#!/bin/bash

# Copyright (C) 2014 CDR-port
# cdr-port@cdr-port.net
# GLOBAL
source funcoes.sh


    clear
    echo " > Instalar CDR-port"
    echo "====================="
    echo "  1)  Instalar CDR-port"
    echo "  2)  Instalar Asterisk"
	echo "  3)  Instalação COMPLETA"
    echo "  0)  Sair"
    echo -n "(0-3) : "
    read OPTION < /dev/tty

ExitFinish=0

while [ $ExitFinish -eq 0 ]; do


	 case $OPTION in

		1)

            #Instalar CDR-port
            clear
            cd /usr/src/
            func_install_req_cdr-port
            func_install_mysql
            func_install_cdr-port
            func_config_asterisk
            bash /usr/src/menu.sh
            ExitFinish=1
		;;

		2)
		    #Instalando ASTERISK
			clear
			func_install_req_asterisk
			func_install_asterisk
            bash /usr/src/menu.sh
			ExitFinish=1
		;;

		3)

            #Instalação COMPLETA
            clear
            cd /usr/src/
            func_install_req_cdr-port
            func_install_req_asterisk
            func_install_mysql
            func_install_cdr-port
            func_install_req_asterisk
            func_install_asterisk
            func_config_asterisk
            bash /usr/src/menu.sh
            ExitFinish=1
		;;

		0)
        	clear
			cd /usr/src/
			rm -rf asterisk*
            rm -rf *.sh
			# Apaga Instalacao
			cd /usr/share/cdrport/cdr-port/
			rm -rf install
			ExitFinish=1
		;;
		*)
	esac
done