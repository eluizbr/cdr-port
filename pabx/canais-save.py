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

## Conexão ao banco MySQL
connection = MySQLdb.connect(host='localhost', user='root', passwd='app2004', db='cdrport')
c = connection.cursor()


exten = asterisk.stats_request('CoreShowChannels')
dados = json.dumps(exten)
#print dados
dados_load = json.loads(dados)
#print dados_load

def real_time():

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
				
				print ChannelState, ChannelStateDesc,  Uniqueid


				if ChannelState != "6":

					x = "SELECT Uniqueid FROM pabx_rt_calls WHERE Uniqueid = " + str(Uniqueid)
					x = c.execute(x)

					if not c.fetchone() is None:
						#print 'O numero %s ja existe'%(Uniqueid)
						atualiza = """UPDATE pabx_rt_calls SET Duration = '%s' WHERE Uniqueid = '%s' """ % (Duration,Uniqueid)
						#print atualiza
						c.execute(atualiza)
						connection.commit()
						

					else:

						SQL_INSERE = ("INSERT INTO pabx_rt_calls"
									"(Event,Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,Language,\
										AccountCode,Context,Exten,Priority,Uniqueid,Application,ApplicationData,Duration,BridgeId)"
									"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

						DADOS = (Event,Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,Language,\
								AccountCode,Context,Exten,Priority,Uniqueid,Application,ApplicationData,Duration,BridgeId)
						c.execute(SQL_INSERE, DADOS)
						connection.commit()
						
				else:

					x = """SELECT Uniqueid FROM pabx_rt_calls WHERE BridgeId = '%s' AND Uniqueid = %s"""  % (BridgeId,Uniqueid)
					#print x
					x = c.execute(x)

					if not c.fetchone() is None:
						
						up = """DELETE FROM pabx_rt_calls WHERE BridgeId != '%s' AND Uniqueid != '%s' """ % (BridgeId,Uniqueid)
						#print up
						c.execute(up)	
						down = "DELETE FROM pabx_rt_calls WHERE BridgeId = '' AND ChannelStateDesc = 'Down' AND Uniqueid = " + str(Uniqueid)
						c.execute(down)					
						ring = "DELETE FROM pabx_rt_calls WHERE BridgeId = '' AND ChannelStateDesc = 'Ring' AND Uniqueid = " + str(Uniqueid)
						c.execute(ring)
						ringing = "DELETE FROM pabx_rt_calls WHERE BridgeId = '' AND ChannelStateDesc = 'Ringing' AND Uniqueid = " + str(Uniqueid)
						c.execute(ringing)
						
						atualiza = """UPDATE pabx_rt_calls SET Duration = '%s' WHERE ChannelStateDesc = 'Up' AND Uniqueid = '%s' """ % (Duration,Uniqueid)
						#print atualiza
						c.execute(atualiza)
						connection.commit()
						

					else:

						SQL_INSERE = ("INSERT INTO pabx_rt_calls"
									"(Event,Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,Language,\
										AccountCode,Context,Exten,Priority,Uniqueid,Application,ApplicationData,Duration,BridgeId)"
									"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

						DADOS = (Event,Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,Language,\
								AccountCode,Context,Exten,Priority,Uniqueid,Application,ApplicationData,Duration,BridgeId)
						c.execute(SQL_INSERE, DADOS)
						connection.commit()
						

			except KeyError as e:
				
				atualiza_1 = "UPDATE pabx_rt_calls SET controle = 1 "
				atualiza_2 = "UPDATE pabx_rt_calls SET ChannelStateDesc = 'Down' "
				#print atualiza
				c.execute(atualiza_1)
				c.execute(atualiza_2)
				connection.commit()
real_time()

'''
def work():

	while True:

		
		time.sleep(1)
		sys.stdout.flush()
		real_time()
		
		print "Current date & time " + time.strftime("%c")

work()
'''


