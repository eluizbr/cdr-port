# coding: utf-8
#!/usr/bin/env python
import threading
import time
import MySQLdb
import asterisk_stats as asterisk
import json
import sys
import random

## Conexão ao banco MySQL
connection = MySQLdb.connect(host='localhost', user='root', passwd='app2004', db='cdrport')
c = connection.cursor()

exten = asterisk.stats_request('CoreShowChannels')
dados = json.dumps(exten)
dados_load = json.loads(dados)

SQL_INSERE = ("INSERT INTO rt_uniqueid"
			"(Uniqueid,ChannelStateDesc)"
			"VALUES (%s,%s)")


for item in dados_load:

	Uniqueid = item['Uniqueid']
	ChannelStateDesc = item['ChannelStateDesc']

	print Uniqueid


	id_unico = "SELECT Uniqueid FROM rt_uniqueid WHERE Uniqueid = "  + (Uniqueid)
	id_unico = c.execute(id_unico)
	id_unico = c.fetchone()
	id_unico = str(id_unico[0])
	print id_unico

	existe = "SELECT Uniqueid FROM rt_uniqueid WHERE Uniqueid != "  + (Uniqueid)
	existe = c.execute(existe)
	existe = c.fetchall()
	print existe

	if not id_unico is None:
		print id_unico

		for existe_v in existe:
			existe_v = str(existe_v[0])
			#print existe_v

			if Uniqueid == existe_v:
				print '%s nao deletar' %Uniqueid
			
			elif Uniqueid != existe_v:

				print '%s e diferente de %s' % (existe_v,Uniqueid)
				delete = "DELETE FROM rt_uniqueid WHERE Uniqueid =  " + (existe_v)
				print delete
				#c.execute(delete)

		

	else:
		DADOS = (Uniqueid,ChannelStateDesc)
		print DADOS
		c.execute(SQL_INSERE, DADOS)
		connection.commit()
	