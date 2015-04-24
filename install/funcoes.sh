#!/bin/bash

# Copyright (C) 2011-2014 ToFalando
#
# Script incialmente desenvolvido por
# Emerson Luiz ( eluizbr@tofalando.com.br )

# Configurar o Branch
BRANCH='master'

func_variaveis () {

echo "`ip addr show eth0 | cut -c16-32 | egrep \"[0-9a-z]{2}[:][0-9a-z]{2}[:][0-9a-z]{2}[:][0-9a-z]{2}[:][0-9a-z]{2}[:][0-9a-z]{2}$\"`" | tr -d ' : ' >/tmp/mac.txt
MAC=$(cat /tmp/mac.txt)
ALEATORIO=$MAC
TOFALANDO="ToFalando-$ALEATORIO"
TOFALANDO2="$ALEATORIO"
echo " $TOFALANDO"
echo "$TOFALANDO2"
export TOFALANDO=$TOFALANDO
export TOFALANDO2=$TOFALANDO2	
	
}





func_host () {
	
		func_variaveis	

			echo "$TOFALANDO" > /etc/hostname

			echo "127.0.0.1	localhost" > /etc/hosts
			IP_LOCAL=$(/sbin/ifconfig | sed -n '2 p' | awk '{print $3}')
			echo "${IP_LOCAL}	$TOFALANDO.tofalando.net	$TOFALANDO" >> /etc/hosts

			echo "

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters" >> /etc/hosts

}




