# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import threading
import time
import MySQLdb
import asterisk_stats as asterisk
import json
import sys

"""
Controle:

0 = Chamando
1 = Falando
2 = Desligou
3 = Ligação morta

"""
#Exten = 3140627330

def valida(Exten=None):
	## Conexão ao banco MySQL
	connection = MySQLdb.connect(host='localhost', user='root', passwd='app2004', db='cdrport')
	c = connection.cursor()

	try:
		numero = "SELECT Exten FROM pabx_rt_calls WHERE Exten = " + str(Exten)
		numero = c.execute(numero)
		numero = c.fetchone()[0]
		numero = numero[:6]

		prefixo = "SELECT prefixo FROM cdr_prefixo WHERE prefixo = " + str(numero)
		prefixo = c.execute(prefixo)
		prefixo = c.fetchone()[0]
		print prefixo


		return 'tronco'

			
	except TypeError as e:

		pass

valida(Exten=3791530792)


