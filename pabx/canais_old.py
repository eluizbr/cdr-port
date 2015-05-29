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

				for i in ChannelState:
					
					#print i
					
					if i != "6":
						print 'entrou em CHAMANDO'

					#if ChannelState != "6":

						x = "SELECT Uniqueid FROM pabx_rt_calls WHERE Uniqueid = " + str(Uniqueid)
						x = c.execute(x)


						if not c.fetchone() is None:
							print 'Ligacao nova ATUALIZANDO RELEGIO!!!'
							print 'O numero %s ja existe'%(Uniqueid)
							atualiza = """UPDATE pabx_rt_calls SET Duration = '%s' WHERE Uniqueid = '%s' AND Application = "Dial" """ % (Duration,Uniqueid)
							atualiza = c.execute(atualiza)
							#print atualiza

							connection.commit()

							status = "SELECT ChannelStateDesc FROM pabx_rt_calls"
							staus = c.execute(status)
							status = c.fetchall()

							for status in status:
								status = str(status[0])

							id_controle = "SELECT controle FROM pabx_rt_calls"
							id_controle = c.execute(id_controle)
							id_controle = c.fetchall()
							id_controle = id_controle


							for control in id_controle:
								control = str(control[0])
								

							id_ring = "SELECT Uniqueid FROM pabx_rt_calls WHERE ChannelStateDesc = 'Ring'"
							id_ring = c.execute(id_ring)
							id_ring = c.fetchall()
							id_ring = id_ring

							id_up = "SELECT Uniqueid FROM pabx_rt_calls WHERE ChannelStateDesc = 'Up' AND Uniqueid != " + str(Uniqueid)
							id_up = c.execute(id_up)
							id_up = c.fetchall()
							id_up = id_up

							
							for id_up  in id_up:
								id_up = str(id_up[0])
								print id_up


								if id_up == id_up and status == "Up":

									
									if control == 4:
										pass
									else:	

										print 'Atualizou para 41'
										atualiza = "UPDATE pabx_rt_calls SET controle = 4 WHERE ChannelStateDesc = 'Up' AND Uniqueid = " + str(id_up)
										print atualiza
										atualiza = c.execute(atualiza)
										dead = """DELETE FROM pabx_rt_calls WHERE controle = 4 """
										print dead
										c.execute(dead)

										print 'Atualizou para 41'
										atualizaz = "UPDATE pabx_rt_calls SET controle = 4 WHERE ChannelStateDesc = 'Ring' AND Uniqueid = " + str(id_up)
										print atualizaz
										atualiza = c.execute(atualizaz)

										connection.commit()
								
								if id_up == id_up and status == "Ring":

									
									if control == 4:
										pass
									
									else:	

										print 'Atualizou para 42'
										atualiza = "UPDATE pabx_rt_calls SET controle = 4 WHERE ChannelStateDesc = 'Ring' AND Uniqueid = " + str(id_up)
										print atualiza
										atualiza = c.execute(atualiza)
										dead = """DELETE FROM pabx_rt_calls WHERE controle = 4 """
										print dead
										c.execute(dead)

										print 'Atualizou para 42'
										atualizaz = "UPDATE pabx_rt_calls SET controle = 4 WHERE ChannelStateDesc = 'Ring' AND Uniqueid = " + str(id_up)
										print atualizaz
										atualiza = c.execute(atualizaz)

										connection.commit()

							for id_ring  in id_ring:
								id_ring = str(id_ring[0])
								print id_ring

								
								if id_ring != Uniqueid and status == "Ring":

									
									if Uniqueid == Uniqueid:
										print 'Atualizou para 43'
										atualiza = "UPDATE pabx_rt_calls SET controle = 4 WHERE ChannelStateDesc = 'Ring' AND Uniqueid = " + str(id_ring)
										print atualiza
										atualiza = c.execute(atualiza)
										dead = """DELETE FROM pabx_rt_calls WHERE controle = 4 """
										print dead
										c.execute(dead)

										print 'Atualizou para 43'
										atualizaz = "UPDATE pabx_rt_calls SET controle = 4 WHERE ChannelStateDesc = 'Ring' AND Uniqueid = " + str(id_ring)
										print atualizaz
										atualiza = c.execute(atualizaz)

										connection.commit()
									
									else:
										pass	


						

						else:
							#print 'Ligacao nova!!!'


							
							if Application == "Dial":
							
								SQL_INSERE = ("INSERT INTO pabx_rt_calls"
											"(Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
												AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId,controle)"
											"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)")

								DADOS = (Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
										AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId)
								c.execute(SQL_INSERE, DADOS)
								connection.commit()
					
					if i == "6":
						print 'entrou em FALANDO'						
						
				#if ChannelState == "6":

						print "procesoo já existe"
						x = """SELECT Uniqueid FROM pabx_rt_calls WHERE Application = "Dial" AND BridgeId = '%s' AND Uniqueid = %s"""  % (BridgeId,Uniqueid)
						print x
						x = c.execute(x)

						if not c.fetchone() is None:
							
							atualiza = """UPDATE pabx_rt_calls SET Duration = '%s' WHERE Application = "Dial" AND ChannelStateDesc = 'Up' AND Uniqueid = '%s' """ % (Duration,Uniqueid)
							print atualiza
							c.execute(atualiza)
							connection.commit()

							status = "SELECT ChannelStateDesc FROM pabx_rt_calls"
							staus = c.execute(status)
							status = c.fetchall()

							for status in status:
								status = str(status[0])

							id_controle = "SELECT controle FROM pabx_rt_calls"
							id_controle = c.execute(id_controle)
							id_controle = c.fetchall()
							id_controle = id_controle


							for control in id_controle:
								control = str(control[0])
								

							id_ring = "SELECT Uniqueid FROM pabx_rt_calls WHERE ChannelStateDesc = 'Ring'"
							id_ring = c.execute(id_ring)
							id_ring = c.fetchall()
							id_ring = id_ring

							id_up = "SELECT Uniqueid FROM pabx_rt_calls WHERE ChannelStateDesc = 'Up' AND Uniqueid != " + str(Uniqueid)
							id_up = c.execute(id_up)
							id_up = c.fetchall()
							id_up = id_up

							for id_up in id_up:
								id_up = str(id_up[0])
								print id_up				

								if id_up == id_up and status == "Up":

									
									if control == 4:
										pass
									
									else:	

										print 'Atualizou para 44'
										atualiza = "UPDATE pabx_rt_calls SET controle = 4 WHERE ChannelStateDesc = 'Up' AND Uniqueid = " + str(id_up)
										print atualiza
										atualiza = c.execute(atualiza)
										dead = """DELETE FROM pabx_rt_calls WHERE controle = 4 """
										print dead
										c.execute(dead)

										connection.commit()
								
								if id_up == id_up and status == "Ring":

									
									if control == 4:
										pass
									
									else:	

										print 'Atualizou para 44'
										atualiza = "UPDATE pabx_rt_calls SET controle = 4 WHERE ChannelStateDesc = 'Ring' AND Uniqueid = " + str(id_up)
										print atualiza
										atualiza = c.execute(atualiza)
										dead = """DELETE FROM pabx_rt_calls WHERE controle = 4 """
										print dead
										c.execute(dead)

										connection.commit()


							for id_ring in id_ring:
								id_ring = str(id_ring[0])
								print 'ID RING é %s' % id_ring

								if id_ring == id_ring and status == "Up":

									
									if control == 4:
										pass
									
									else:	

										print 'Atualizou para 45.1'
										atualiza = "UPDATE pabx_rt_calls SET controle = 4 WHERE ChannelStateDesc = 'Ring' AND Uniqueid = " + str(id_ring)
										print atualiza
										atualiza = c.execute(atualiza)
										dead = """DELETE FROM pabx_rt_calls WHERE controle = 4 """
										print dead
										c.execute(dead)

										connection.commit()
								
								if id_ring is not Uniqueid and status == "Ring":

									
									if id_ring == Uniqueid:
										pass

									
									else:	

										print '---------------------------------'
										print 'ID RING nao existe %s' % id_ring
										print 'ID RING existe %s' % Uniqueid

										print 'Atualizou para 45.2.1'
										atualiza = "UPDATE pabx_rt_calls SET controle = 4 WHERE ChannelStateDesc = 'Ring' AND Uniqueid = " + str(id_ring)
										print atualiza
										atualiza = c.execute(atualiza)
										dead = """DELETE FROM pabx_rt_calls WHERE controle = 4 """
										print dead
										c.execute(dead)

										connection.commit()
										print '---------------------------------'
						else:

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
				
				atualiza_1 = "UPDATE pabx_rt_calls SET controle = 3 "
				atualiza_2 = "UPDATE pabx_rt_calls SET ChannelStateDesc = 'Dead' "
				print atualiza_1
				c.execute(atualiza_1)
				c.execute(atualiza_2)

				
				dead = """DELETE FROM pabx_rt_calls WHERE ChannelStateDesc = 'Dead' """
				#print dead
				c.execute(dead)
				

				connection.commit()

real_time()


