# -*- coding: UTF-8 -*-
import MySQLdb
from datetime import datetime, timedelta, time
import os
import commands

## Conexão ao banco MySQL
connection = MySQLdb.connect(host='localhost', user='root', passwd='SENHA_DB', db='cdrport')
c = connection.cursor()
## Configurções padrão para data e hora
hoje = datetime.now()
proximo_mes = hoje + timedelta(days=31)

uuid = commands.getoutput('dmidecode -s system-uuid')
system_number = commands.getoutput('dmidecode -s system-serial-number')
system_name = commands.getoutput('dmidecode -s system-product-name')
mac = commands.getoutput('cat /sys/class/net/eth?/address')
frequencia = commands.getoutput('dmidecode -s  processor-frequency')


def registra():

	SQL_INSERE = ("INSERT INTO cdr_info" 
	            "(uuid, system_number, system_name, mac, frequencia, data_ativacao, data_expira, ativo)" 
	            "VALUES  (%s, %s, %s, %s, %s, %s, %s, 1)")
	DADOS = (uuid, system_number, system_name, mac, frequencia, hoje, proximo_mes)
	c.execute(SQL_INSERE, DADOS)
	#print 'Operadora e %s, %s, %s, %s, %s, %s, %s, 1'%(DADOS)
	connection.commit()

def main():

	x = "SELECT uuid FROM cdr_info WHERE uuid ='%s' " % uuid
	x = c.execute(x)
	if not c.fetchone() is None:
		print 'Sistema já ativo'
	else:
		registra()
main()
