# -*- coding: UTF-8 -*-
import MySQLdb
import time
import datetime
import sys



## Conexão ao banco MySQL
connection = MySQLdb.connect(host='localhost', user='root', passwd='app2004', db='cdrport')
c = connection.cursor()

## Configurções padrão para data e hora
data_atual = datetime.datetime.now()
hora = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%H:%M:%S'))
data_atual1 = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d'))


def consulta_numero():
	numero = sys.argv[1]

	if len(numero) == 10:

		numero = sys.argv[1]
		x = "SELECT numero FROM portados WHERE numero = " + str(numero)
		x = c.execute(x)
	    
		if not c.fetchone() is None:
			x = "SELECT rn1 FROM portados WHERE numero = " + str(numero)
			x = c.execute(x)
			x = c.fetchone()[0]
			return '0' + str(x)[3:]
		else:
			numero = sys.argv[1]
			prefixo = sys.argv[1][:6]
			x = "SELECT rn1 FROM nao_portados WHERE prefixo = " + str(prefixo)
			x = c.execute(x)
			x = c.fetchone()[0]
			return '0' + str(x)[3:]

	if len(numero) == 11:

		numero = sys.argv[1]
		x = "SELECT numero FROM portados WHERE numero = " + str(numero)
		x = c.execute(x)
	    
		if not c.fetchone() is None:
			x = "SELECT rn1 FROM portados WHERE numero = " + str(numero)
			x = c.execute(x)
			x = c.fetchone()[0]
			return '0' + str(x)[3:]
		else:
			numero = sys.argv[1]
			prefixo = sys.argv[1][:7]
			x = "SELECT rn1 FROM nao_portados WHERE prefixo = " + str(prefixo)
			x = c.execute(x)
			x = c.fetchone()[0]
			return '0' + str(x)[3:]

consulta_numero()

print consulta_numero()