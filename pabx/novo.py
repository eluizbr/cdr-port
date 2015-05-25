# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import threading
import time
import MySQLdb
import asterisk_stats as asterisk
import json
import sys
import random

exten = asterisk.stats_request('CoreShowChannels')
dados = json.dumps(exten)
dados_load = json.loads(dados)

## Conexão ao banco MySQL
connection = MySQLdb.connect(host='localhost', user='root', passwd='app2004', db='cdrport')
c = connection.cursor()

id_unico = '' # UniqueID de cada ligação
staus_licagao = '' # Status da Ligacao (Se esta chamando, falando, desligado)

for item in dados_load:

		try:


			Event = item['Event']
			Channel = item['Channel']
			ChannelState = item['ChannelState']
			ChannelStateDesc = item['ChannelStateDesc']
			CallerIDNum = item['CallerIDNum']
			CallerIDName = item['CallerIDName']
			ConnectedLineNum = item['ConnectedLineNum']
			ConnectedLineName = item['ConnectedLineName']
			Language = item['Language']
			AccountCode = item['AccountCode']
			Context = item['Context']
			Exten = item['Exten']
			Priority = item['Priority']
			Uniqueid = item['Uniqueid']
			Application = item['Application']
			ApplicationData = item['ApplicationData']
			Duration = item['Duration']
			BridgeId = item['BridgeId']

			#print Uniqueid

			id_unico += Uniqueid
			staus_licagao += ChannelState

		except KeyError as e:
			pass


# INICIO Bloco trata ligação MORTA em estdo de RING			
def apaga_ligacao_morta_ring():

	try:
		query = ''

		for item in dados_load:

			Uniqueid = item['Uniqueid']
			ChannelStateDesc = item['ChannelStateDesc']
			query += " AND Uniqueid != " + Uniqueid

		id_falando = "SELECT Uniqueid FROM pabx_rt_calls WHERE ChannelState !=9 %s" % query
		print id_falando
		id_falando = c.execute(id_falando)
		id_falando = c.fetchall()

		id_morto = ''

		for id_falando_v in id_falando:
			id_falando_v = str(id_falando_v[0],)
			id_morto = id_falando_v
			ring = "DELETE FROM pabx_rt_calls WHERE Uniqueid = %s" % id_morto
			print ring
			c.execute(ring)
			connection.commit()
	
	except KeyError as e:
		pass
		

#apaga_ligacao_morta_ring()
# FIM Bloco trata ligação MORTA em estdo de RING

def insere_ramal():

	origem_in = "SELECT CallerIDNum FROM pabx_rt_calls"
	origem_in = c.execute(origem_in)
	origem_in = c.fetchall()
	
	ramal_livre = "SELECT name FROM vw_sipregs WHERE name not in (SELECT CallerIDNum FROM pabx_rt_calls)"
	ramal_livre = c.execute(ramal_livre)
	ramal_livre = c.fetchall()

	for ramal_livre_v in ramal_livre:
		ramal_livre_v = str(ramal_livre_v[0])
		print ramal_livre_v	

		ipaddr = "SELECT ipaddr FROM vw_sipregs WHERE name = " + str(ramal_livre_v)
		ipaddr = c.execute(ipaddr)
		ipaddr = c.fetchone()[0]
		print ipaddr

		lastms = "SELECT lastms FROM vw_sipregs WHERE name = " + str(ramal_livre_v)
		lastms = c.execute(lastms)
		lastms = c.fetchone()[0]
		print lastms
		numero = random.randint(7500000000.000, 8500000000.000)
		print numero
		print ramal_livre_v, ipaddr, lastms

		SQL_INSERE = ("INSERT INTO pabx_rt_calls"
					"(CallerIDNum,ChannelState,ChannelStateDesc,Uniqueid,Duration,controle,ipaddr,lastms)"
					"VALUES (%s,9,'Dead',%s,'00:00:00',0,%s,%s)")

		DADOS = (ramal_livre_v,numero,ipaddr,lastms)
		c.execute(SQL_INSERE, DADOS)
		connection.commit()	

#insere_ramal()


# INICIO Bloco tratamento de ligacoes CHAMANDO
def insere_ligacao_chamando():
	#insere_ramal()
	apaga_ligacao_morta_ring()

	exten = asterisk.stats_request('CoreShowChannels')
	dados = json.dumps(exten)
	dados_load = json.loads(dados)

	for item in dados_load:

			try:

				Application = item['Application']
				ChannelState = item['ChannelState']
				ChannelStateDesc = item['ChannelStateDesc']
				Uniqueid = item['Uniqueid']
				CallerIDNum = item['CallerIDNum']
				Exten = item['Exten']

				if ChannelState != '6':
					#print Uniqueid
					chamando = "SELECT Uniqueid FROM pabx_rt_calls WHERE Uniqueid = " + str(Uniqueid)
					chamando = c.execute(chamando)
					chamando = c.fetchone()



					if not chamando is None:

						print 'Ligacao nova ATUALIZANDO RELEGIO!!!'
						print 'O numero %s ja existe'%(Uniqueid)
						atualiza = """UPDATE pabx_rt_calls SET Duration = '%s' WHERE Uniqueid = '%s' AND Application = "Dial" """ % (Duration,Uniqueid)
						print atualiza
						atualiza = c.execute(atualiza)
						#print atualiza

						connection.commit()					



					else:

						print CallerIDNum
						ramal_logado = "SELECT CallerIDNum FROM pabx_rt_calls WHERE ChannelState = 9 AND ChannelStateDesc = 'Dead'"
						ramal_logado = c.execute(ramal_logado)
						ramal_logado = c.fetchall()
						for ramal_logado_v in ramal_logado:
							ramal_logado_v = str(ramal_logado_v[0])
							#print ramal_logado_v
							deleta_1 = "DELETE FROM pabx_rt_calls WHERE ChannelState = 9 AND ChannelStateDesc = 'Dead' AND CallerIDNum = " + str(CallerIDNum)
							deleta_2 = "DELETE FROM pabx_rt_calls WHERE ChannelState = 9 AND ChannelStateDesc = 'Dead' AND CallerIDNum = " + str(Exten)
							print deleta_2
							deleta_1 = c.execute(deleta_1)
							deleta_2 = c.execute(deleta_2)
							connection.commit()

						print 'Inserindo NOVA LIGACAO'
						if Application == "Dial":
						
							SQL_INSERE = ("INSERT INTO pabx_rt_calls"
										"(Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
											AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId,controle)"
										"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)")

							DADOS = (Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
									AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId)
							c.execute(SQL_INSERE, DADOS)
							connection.commit()

			except KeyError as e:

				ring = "DELETE FROM pabx_rt_calls WHERE ChannelStateDesc = 'Ring'"

				c.execute(ring)
				ringing = "DELETE FROM pabx_rt_calls WHERE ChannelStateDesc = 'Ringing'"

				c.execute(ringing)
				up = "DELETE FROM pabx_rt_calls WHERE ChannelStateDesc = 'Up'"

				c.execute(up)
				down = "DELETE FROM pabx_rt_calls WHERE ChannelStateDesc = 'Down'"

				c.execute(down)
				connection.commit()


insere_ligacao_chamando()
# FIM Bloco tratamento de ligacoes CHAMANDO

# INICIO Bloco tratamento de ligacoes FALANDO
def insere_ligacao_falando():

	apaga_ligacao_morta_ring()
	
	exten = asterisk.stats_request('CoreShowChannels')
	dados = json.dumps(exten)
	dados_load = json.loads(dados)

	for item in dados_load:

			try:

				Application = item['Application']
				ChannelState = item['ChannelState']
				ChannelStateDesc = item['ChannelStateDesc']
				Uniqueid = item['Uniqueid']
				CallerIDNum = item['CallerIDNum']
				Exten = item['Exten']
				Duration = item['Duration']

				if ChannelState == '6':
					print 'Entrou em FALANDO'


					falando = "SELECT Uniqueid FROM pabx_rt_calls WHERE Uniqueid = " + str(Uniqueid)
					falando = c.execute(falando)
					falando = c.fetchone()

					ramal_logado = "SELECT CallerIDNum FROM pabx_rt_calls WHERE ChannelState = 9 AND ChannelStateDesc = 'Dead'"
					ramal_logado = c.execute(ramal_logado)
					ramal_logado = c.fetchall()

					for ramal_logado_v in ramal_logado:
						ramal_logado_v = str(ramal_logado_v[0])
						#print ramal_logado_v
						deleta_1 = "DELETE FROM pabx_rt_calls WHERE ChannelState = 9 AND ChannelStateDesc = 'Dead' AND CallerIDNum = " + str(CallerIDNum)
						#print deleta_2
						deleta_1 = c.execute(deleta_1)

						connection.commit()

					if not falando is None:
						print falando
						#print 'Ligacao nova ATUALIZANDO RELEGIO!!!'
						#print 'O numero %s ja existe'%(Uniqueid)
						atualiza = """UPDATE pabx_rt_calls SET Duration = '%s' WHERE Uniqueid = '%s' AND Application = "Dial" """ % (Duration,Uniqueid)
						#print atualiza
						atualiza = c.execute(atualiza)
						#print atualiza
						connection.commit()					


					else:


						exten = asterisk.stats_request('CoreShowChannels')
						dados = json.dumps(exten)
						dados_load = json.loads(dados)

						for item in dados_load:

							Channel = item['Channel']
							ChannelState = item['ChannelState']
							ChannelStateDesc = item['ChannelStateDesc']
							CallerIDNum = item['CallerIDNum']
							CallerIDName = item['CallerIDName']
							ConnectedLineNum = item['ConnectedLineNum']
							ConnectedLineName = item['ConnectedLineName']
							Exten = item['Exten']
							Uniqueid = item['Uniqueid']
							Application = item['Application']
							ApplicationData = item['ApplicationData']
							Duration = item['Duration']
							BridgeId = item['BridgeId']

							print 'Inserindo NOVO FALANDO'

							if Application == "Dial":

								SQL_INSERE = ("INSERT INTO pabx_rt_calls"
											"(Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
												AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId,controle)"
											"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,1)")

								DADOS = (Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
										AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId)
								c.execute(SQL_INSERE, DADOS)

								connection.commit()

			except KeyError as e:

				ring = "DELETE FROM pabx_rt_calls WHERE ChannelStateDesc = 'Ring'"

				c.execute(ring)
				ringing = "DELETE FROM pabx_rt_calls WHERE ChannelStateDesc = 'Ringing'"

				c.execute(ringing)
				up = "DELETE FROM pabx_rt_calls WHERE ChannelStateDesc = 'Up'"

				c.execute(up)
				down = "DELETE FROM pabx_rt_calls WHERE ChannelStateDesc = 'Down'"

				c.execute(down)
				connection.commit()


insere_ligacao_falando()
# FIM Bloco tratamento de ligacoes FALANDO



