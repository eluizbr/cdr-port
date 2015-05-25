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
query = ''

for item in dados_load:

	Uniqueid = item['Uniqueid']
	ChannelStateDesc = item['ChannelStateDesc']
	query += " AND Uniqueid != " + Uniqueid
print query



id_falando = "SELECT Uniqueid FROM pabx_rt_calls WHERE ChannelState !=9 %s" % query
print id_falando
id_falando = c.execute(id_falando)
id_falando = c.fetchall()

id_morto = ''

for id_falando_v in id_falando:
	id_falando_v = str(id_falando_v[0],)
	id_morto += '' + id_falando_v + ''

print id_morto

ring = "DELETE FROM rt_uniqueid WHERE Uniqueid in (%s)" % id_morto
print ring
#c.execute(ring)
#connection.commit()







	


