# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import MySQLdb
import asterisk_stats as asterisk
import json

## Conexão ao banco MySQL
connection = MySQLdb.connect(host='localhost', user='root', passwd='app2004', db='cdrport')
c = connection.cursor()

exten = asterisk.stats_request('CoreShowChannels')
dados = json.dumps(exten)
dados_load = json.loads(dados)

id_unico = [] # UniqueID de cada ligação
status_canal = [] # Mostra o status do Canal (4 e 5 CHAMANDO, 6 FALANDO)

for item in dados_load:
		try:
			Uniqueid = item['Uniqueid']
			id_unico.append(Uniqueid)
			Application = item['Application']
			ChannelState = item['ChannelState']
			status_canal.append(ChannelState)
			ChannelStateDesc = item['ChannelStateDesc']
			CallerIDNum = item['CallerIDNum']
			Exten = item['Exten']
			Duration = item['Duration']


	
		except KeyError as e:
			pass


contador = -1
while Uniqueid and contador < len(id_unico):
	try:
		contador = contador + 1
		print id_unico
		id = id_unico[contador]
		print id
		banco = "SELECT Uniqueid FROM pabx_rt_calls WHERE ChannelState !=9 AND Uniqueid != %s" % id
		print banco
		banco = c.execute(banco)
		banco = c.fetchall()
		print banco

		if id == Uniqueid:
			print 'ok %s' % Uniqueid
		else:
			print 'nao %s' % Uniqueid
		 
	except IndexError as e:
		pass	






