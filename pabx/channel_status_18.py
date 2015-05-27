# -*- coding: UTF-8 -*-
#!/usr/bin/env python



import asterisk_stats as asterisk
import json

exten = asterisk.stats_request('CoreShowChannels')
dados = json.dumps(exten)
dados_load = json.loads(dados)

id_unico = []
origem_unico = []
dial_unico = []
channelDESC_unico = []
channelSTATE_unico = []
destino_unico = []

for item in dados_load:

		try:
			
			Event = item['Event']
			Channel = item['Channel']
			ChannelState = item['ChannelState']
			channelSTATE_unico.append(ChannelState)
			ChannelStateDesc = item['ChannelStateDesc']
			channelDESC_unico .append(ChannelStateDesc)
			CallerIDNum = item['CallerIDnum']
			origem_unico.append(CallerIDNum)
			CallerIDName = item['CallerIDname']
			ConnectedLineNum = item['ConnectedLineNum']
			ConnectedLineName = item['ConnectedLineName']
			AccountCode = item['AccountCode']
			Context = item['Context']
			Exten = item['Extension']
			destino_unico.append(Exten)
			Priority = item['Priority']
			Uniqueid = item['UniqueID']
			id_unico.append(Uniqueid)
			Application = item['Application']
			dial_unico.append(Application)
			ApplicationData = item['ApplicationData']
			Duration = item['Duration']
			BridgeId = item['BridgedUniqueID']
			print Uniqueid

		except KeyError as e:
			pass

def validar_uniqueid():

	'''
	Esta função retorna ao MySQL os Uniqueid a serem comparados
	'''
	contador = -1
	var = ''
	while contador < len(Uniqueid):
		try:
			contador = contador + 1
			var += ' AND Uniqueid != ' + id_unico[contador]
		except IndexError as e:
			pass

	return var
