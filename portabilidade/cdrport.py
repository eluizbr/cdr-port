# -*- coding: UTF-8 -*-
import MySQLdb
import sys

## Conexão ao banco MySQL
connection = MySQLdb.connect(host='localhost', user='root', passwd='app2004', db='cdrport')
c = connection.cursor()


def consulta_numero():
	numero = sys.argv[1]

	if len(numero) == 8:
		numero = sys.argv[1]
		ddd = "SELECT ddd FROM cdr_config_local" 
		ddd = c.execute(ddd)
		ddd = c.fetchone()[0]
		numero_ddd = str(ddd)+str(numero)
		
		x = "SELECT numero FROM portados WHERE numero = " + str(numero_ddd)
		x = c.execute(x)
	    
		if not c.fetchone() is None:
			x = "SELECT rn1 FROM portados WHERE numero = " + str(numero_ddd)
			x = c.execute(x)
			x = c.fetchone()[0]
			print 'numero portado'
			return '0' + str(x)[3:]
		else:
			numero = numero_ddd
			prefixo = numero_ddd[:6]
			x = "SELECT rn1 FROM nao_portados WHERE prefixo = " + str(prefixo)
			x = c.execute(x)
			x = c.fetchone()[0]
			return '0' + str(x)[3:]

	if len(numero) == 9:
		numero = sys.argv[1]
		ddd = "SELECT ddd FROM cdr_config_local" 
		ddd = c.execute(ddd)
		ddd = c.fetchone()[0]
		numero_ddd = str(ddd)+str(numero)
		
		x = "SELECT numero FROM portados WHERE numero = " + str(numero_ddd)
		x = c.execute(x)
	    
		if not c.fetchone() is None:
			x = "SELECT rn1 FROM portados WHERE numero = " + str(numero_ddd)
			x = c.execute(x)
			x = c.fetchone()[0]
			print 'numero portado'
			return '0' + str(x)[3:]
		else:
			numero = numero_ddd
			prefixo = numero_ddd[:7]
			x = "SELECT rn1 FROM nao_portados WHERE prefixo = " + str(prefixo)
			x = c.execute(x)
			x = c.fetchone()[0]
			return '0' + str(x)[3:]

	if len(numero) == 10:

		numero = sys.argv[1]
		x = "SELECT numero FROM portados WHERE numero = " + str(numero)
		x = c.execute(x)
	    
		if not c.fetchone() is None:
			x = "SELECT rn1 FROM portados WHERE numero = " + str(numero)
			x = c.execute(x)
			x = c.fetchone()[0]
			print 'numero portado'
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
			print 'numero portado'
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