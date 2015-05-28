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

id_unico = []
origem_unico = []
dial_unico = []
channelDESC_unico = []
channelSTATE_unico = []
destino_unico = []
duracao_unico = []

for item in dados_load:

		try:
			
			Event = item['Event']
			Channel = item['Channel']
			ChannelState = item['ChannelState']
			channelSTATE_unico.append(ChannelState)
			ChannelStateDesc = item['ChannelStateDesc']
			channelDESC_unico .append(ChannelStateDesc)
			CallerIDNum = item['CallerIDNum']
			origem_unico.append(CallerIDNum)
			CallerIDName = item['CallerIDName']
			ConnectedLineNum = item['ConnectedLineNum']
			ConnectedLineName = item['ConnectedLineName']
			Language = item['Language']
			AccountCode = item['AccountCode']
			Context = item['Context']
			Exten = item['Exten']
			destino_unico.append(Exten)
			Priority = item['Priority']
			Uniqueid = item['Uniqueid']
			id_unico.append(Uniqueid)
			Application = item['Application']
			dial_unico.append(Application)
			ApplicationData = item['ApplicationData']
			Duration = item['Duration']
			duracao_unico.append(Duration)
			BridgeId = item['BridgeId']

		except KeyError as e:
			pass

def validar_uniqueid():

	'''
	Esta função retorna ao MySQL os Uniqueid a serem apagados.
	'''
	
	try:
		contador = -1
		var = ''
		while contador < len(Uniqueid):
			try:
				contador = contador + 1
				var += ' AND Uniqueid != ' + id_unico[contador]
			except IndexError as e:
				pass

		return var

	except KeyError as e:
		pass

def uniqueid_existente(uniqueid=None):

	'''
	Esta função retorna se Uniqueid existe. Se sim. ele retorna ele mesmo.
	'''
	try:

		sql = "SELECT Uniqueid FROM TMP_canais WHERE Uniqueid = %s" % uniqueid
		#print sql
		sql = c.execute(sql)
		sql = c.fetchone()[0]
		#print sql
		return sql

	except Exception:
		pass

#uniqueid_existente(1432820460.3)


def ligando_para(ramal=None):

	'''
	Esta função tem como objetivo, retorna com que o ramal esta ligando.
	Uso:
		VAR = ligando_para(ramal)
	'''

	try:

		sql = "SELECT Exten FROM TMP_canais WHERE CallerIDNum = %s AND ChannelStateDesc = 'Ring'" % ramal
		#print sql
		sql = c.execute(sql)
		sql = c.fetchone()[0]
		#print sql
		return sql

	except Exception:
		return None

#ligando_para(300)

def falando_com(ramal=None):

	'''
	Esta função tem como objetivo, retorna com que o ramal esta falando.
	Uso:
		var = falando_com(ramal)
	'''

	try:

		sql = "SELECT Exten FROM TMP_canais WHERE CallerIDNum = %s AND ChannelStateDesc = 'Up'" % ramal
		#print sql
		sql = c.execute(sql)
		sql = c.fetchone()[0]
		#print sql
		return sql

	except Exception:
		return None

#falando_com(300)

def status_ligacao(ramal=None):

	'''
	Esta função tem como objetivo retornar o status da ligacao.
	Status possiveis:
	4 ou 5 = Ring / Ringing
	6 = Up (Falando)
	Uso:
		var = status_ligacao(ramal)
	'''

	try:

		sql = "SELECT ChannelState FROM TMP_canais WHERE CallerIDNum = %s" % ramal
		#print sql
		sql = c.execute(sql)
		sql = c.fetchone()[0]
		#print sql
		return sql

	except Exception:
		return None

#status_ligacao(300)




