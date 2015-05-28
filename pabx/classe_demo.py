# -*- coding: UTF-8 -*-
#!/usr/bin/env python


import MySQLdb
import asterisk_stats as asterisk
import channel_status_18 as canais
import json
import random



## Conexão ao banco MySQL
connection = MySQLdb.connect(host='localhost', user='root', passwd='app2004', db='cdrport')
c = connection.cursor()


class Ramais:
	'''
	Esta classe, trata como esta o status atual do ramal. Ela trabalha quando 
	ramal esta em Stand By, e quando esta em ligação.
	
	'''

	def __init__(self,ramal):
		'''
		Esta função insere o ramal no MySQL quando ele incia uma ligação. Alterando seu status:
		Controle: 8 - Ramal em Stand By, 9 - Ramal em reservar (em ligação)
		'''

		self.ramal = ramal

	def origem(self,ramal):


		sql = "SELECT CallerIDNum FROM TMP_canais WHERE CallerIDNum = %s AND ChannelStateDesc = 'Ring'" % self.ramal
		#print sql
		sql = c.execute(sql)
		sql = c.fetchone()[0]
		print sql
		return sql



	def destino(self,ramal):


		sql = "SELECT Exten FROM TMP_canais WHERE CallerIDNum = %s AND ChannelStateDesc = 'Ring'" % self.ramal
		#print sql
		sql = c.execute(sql)
		sql = c.fetchone()[0]
		print sql
		return sql


origem = Ramais(300)
origem = origem.origem(300)
destino = Ramais(300)
destino = destino.destino(300)



