# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import threading
import time
import MySQLdb
import asterisk_stats as asterisk
import json
import sys
import random

"""
Controle:

0 = Chamando
1 = Falando
2 = Desligou
3 = Ligação morta

"""
#Exten = 3140627330
exten = asterisk.stats_request('CoreShowChannels')
dados = json.dumps(exten)
#print dados
dados_load = json.loads(dados)
#print dados_load
'''
for item in dados_load:


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

	#print CallerIDNum
'''

## Conexão ao banco MySQL
connection = MySQLdb.connect(host='localhost', user='root', passwd='app2004', db='cdrport')
c = connection.cursor()

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
		#print ipaddr

		lastms = "SELECT lastms FROM vw_sipregs WHERE name = " + str(ramal_livre_v)
		lastms = c.execute(lastms)
		lastms = c.fetchone()[0]
		#print lastms
		numero = random.randint(7500000000.000, 8500000000.000)
		print numero
		print ramal_livre_v, ipaddr, lastms

		SQL_INSERE = ("INSERT INTO pabx_rt_calls"
					"(CallerIDNum,ChannelState,ChannelStateDesc,Uniqueid,Duration,controle,ipaddr,lastms)"
					"VALUES (%s,9,'Dead',%s,'00:00:00',0,%s,%s)")

		DADOS = (ramal_livre_v,numero,ipaddr,lastms)
		c.execute(SQL_INSERE, DADOS)
		connection.commit()	



def consulta_ramal():

	try:

		exten = asterisk.stats_request('CoreShowChannels')
		dados = json.dumps(exten)
		#print dados
		dados_load = json.loads(dados)
		#print dados_load
		for item in dados_load:


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

			#print CallerIDNum, ChannelState, ChannelStateDesc

			ramal_logado = "SELECT CallerIDNum FROM pabx_rt_calls WHERE ChannelState = 9 AND ChannelStateDesc = 'Dead'"
			ramal_logado = c.execute(ramal_logado)
			ramal_logado = c.fetchall()

			ramal_chamando = "SELECT CallerIDNum FROM pabx_rt_calls WHERE ChannelState != 6 AND ChannelStateDesc = 'Ring'"
			ramal_chamando = c.execute(ramal_chamando)
			ramal_chamando = c.fetchall()

			ramal_falando = "SELECT CallerIDNum FROM pabx_rt_calls WHERE ChannelState = 6 AND ChannelStateDesc = 'Up'"
			ramal_falando = c.execute(ramal_falando)
			ramal_falando = c.fetchall()

			for i in ChannelState:
				
				#print i
				
				if i != "6":
					print 'entrou em CHAMANDO'


					for ramal_logado_v in ramal_logado:
						ramal_logado_v = str(ramal_logado_v[0])
						print 'aqui 1'

						print Uniqueid
						ring = "DELETE FROM pabx_rt_calls WHERE ChannelStateDesc = 'Ring' AND Uniqueid =  " + str(Uniqueid)
						print ring
						c.execute(ring)
						connection.commit()

						'''
						if ramal_logado_v == CallerIDNum and ChannelState != 6:
							print 'aqui 2'
							print 'Ramal %s inciando ligacao <---------' %ramal_logado_v

							deleta = "DELETE FROM pabx_rt_calls WHERE ChannelState = 9 AND ChannelStateDesc = 'Dead' AND CallerIDNum = " + str(ramal_logado_v)
							print deleta
							deleta = c.execute(deleta)
							connection.commit()

							if Application == "Dial":
								print 'aqui 3'
								SQL_INSERE = ("INSERT INTO pabx_rt_calls"
											"(Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
												AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId,controle)"
											"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)")

								DADOS = (Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
										AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId)
								c.execute(SQL_INSERE, DADOS)
								connection.commit()
						'''
						if ChannelState == '4' and ChannelStateDesc == 'Ring' and Uniqueid != '':
							print 'STATUS RING...'

							print 'Ligacao nova ATUALIZANDO RELEGIO CHMANADO!!!'
							print Uniqueid
							print Duration
							atualiza = """UPDATE pabx_rt_calls SET Duration = '%s' WHERE Uniqueid = '%s' AND Application = 'Dial' AND ChannelStateDesc = 'Ring' """ % (Duration,Uniqueid)
							atualiza = c.execute(atualiza)
							connection.commit()

							if ramal_logado_v == CallerIDNum and ChannelState != 6:
								print 'aqui 2'
								print 'Ramal %s inciando ligacao <---------' %ramal_logado_v

								deleta = "DELETE FROM pabx_rt_calls WHERE ChannelState = 9 AND ChannelStateDesc = 'Dead' AND CallerIDNum = " + str(ramal_logado_v)
								print deleta
								deleta = c.execute(deleta)
								connection.commit()

							if Application == "Dial":
								print 'aqui 3'
								SQL_INSERE = ("INSERT INTO pabx_rt_calls"
											"(Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
												AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId,controle)"
											"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)")

								DADOS = (Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
										AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId)
								c.execute(SQL_INSERE, DADOS)
								connection.commit()


					for ramal_chamando_v in ramal_chamando:
						ramal_chamando_v = str(ramal_chamando_v[0])
						print ramal_chamando_v	
						
						if ramal_chamando_v == CallerIDNum and ChannelState != 6:
							print 'aqui 4'





				if i == "6":
					print 'entrou em FALANDO'	

					if ChannelState == '6' and ChannelStateDesc == 'Up':
						print 'aqui 5'
						print 'ELSE'
						#print "procesoo já existe"
						dial = """SELECT Uniqueid FROM pabx_rt_calls WHERE Application = "Dial" AND BridgeId = '%s' AND Uniqueid = %s"""  % (BridgeId,Uniqueid)
						#print dial
						dial = c.execute(dial)

						if not c.fetchone() is None:
							print 'aqui 5.1'
							#print CallerIDNum
			
							ramal_falando = "SELECT CallerIDNum FROM pabx_rt_calls WHERE ChannelState = 6 AND Application = 'Dial' AND ChannelStateDesc = 'Up'"
							ramal_falando = c.execute(ramal_falando)
							ramal_falando = c.fetchall()

							print Uniqueid
							ring = "DELETE FROM pabx_rt_calls WHERE ChannelStateDesc = 'Ring' AND Uniqueid =  " + str(Uniqueid)
							print ring
							c.execute(ring)


						else:


							if Application == "Dial":
								print 'aqui 6'

							
								SQL_INSERE = ("INSERT INTO pabx_rt_calls"
											"(Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
												AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId,controle)"
											"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,1)")

								DADOS = (Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
										AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId)
								c.execute(SQL_INSERE, DADOS)
								connection.commit()

						
						for ramal_falando_v in ramal_falando:
							print 'aqui 7'


							ramal_falando_v = str(ramal_falando_v[0])
							print 'Ramal %s FALANDO <---------' %ramal_falando_v
							print 'Ligacao nova ATUALIZANDO RELEGIO FALANDO!!!'
							atualiza = """UPDATE pabx_rt_calls SET Duration = '%s' WHERE Uniqueid = '%s' AND Application = "Dial" """ % (Duration,Uniqueid)
							atualiza = c.execute(atualiza)
							connection.commit()
							#print atualiza
			

	except KeyError as e:
		
		print 'inseriu..'
		up = """DELETE FROM pabx_rt_calls WHERE ChannelStateDesc = 'Up' """
		c.execute(up)
		
		ring = """DELETE FROM pabx_rt_calls WHERE ChannelStateDesc = 'Ring' """
		c.execute(ring)
		
		insere_ramal()
		


consulta_ramal()











