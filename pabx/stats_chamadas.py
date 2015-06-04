# -*- coding: UTF-8 -*-
#!/usr/bin/env python


import MySQLdb
import funcoes as funcao
import channel_status as canais
import canais_tmp
import globais


## Conexão ao banco MySQL
connection = MySQLdb.connect(host=globais.host, user=globais.user, passwd=globais.password, db=globais.db)
c = connection.cursor()

def insere_chamada():

	loop = len(canais.origem_unico)
	loop = loop - 1

	try:

		contador = -1
		while contador < loop:
			

				contador = contador +1
				unico = canais.id_unico[contador]
				state = canais.channelSTATE_unico[contador]
				canal = canais.channel_unico[contador]
				CallerIDName = canais.CallerIDName_unico[contador]
				ConnectedLineNum = canais.ConnectedLineNum_unico[contador]
				ConnectedLineName = canais.ConnectedLineName_unico[contador]
				AccountCode = canais.AccountCode_unico[contador]
				Context = canais.Context_uinico[contador]
				Priority = canais.Priority_unico[contador]
				origem = canais.origem_unico[contador]
				dial = canais.dial_unico[contador]
				channelDesc = canais.channelDESC_unico[contador]
				channelState = canais.channelSTATE_unico[contador]
				destino = canais.destino_unico[contador]
				Duration = canais.duracao_unico[contador]
				ApplicationData = canais.ApplicationData_unico[contador]
				BridgeId = canais.BridgeId_unico[contador]

				print unico
				x = canais.uniqueid_existente(unico)
				x = x
				print 'x é %s' % x

				if state == '4' or '5':
					#print  'alterando o status para 4'
					#print x, unico
					if unico != unico:

						atualiza_ring = """UPDATE pabx_rt_calls SET Duration = '%s' WHERE Uniqueid = '%s' AND ChannelStateDesc = 'Ring' """ % (Duration,unico)
						#print atualiza_ring
						atualiza_ring = c.execute(atualiza_ring)
						connection.commit()
						atualiza_ringing = """UPDATE pabx_rt_calls SET Duration = '%s' WHERE Uniqueid = '%s' AND ChannelStateDesc = 'Ringing' """ % (Duration,unico)
						#print atualiza_ringing
						atualiza_ringing = c.execute(atualiza_ringing)
						#print atualiza
						connection.commit()

					else:

						print 'inserindo chamanda'
						apaga_origem = "DELETE FROM pabx_rt_calls WHERE ChannelState = 9 AND CallerIDNum = %s" %origem
						#print apaga_origem
						apaga_origem = c.execute(apaga_origem)
						connection.commit()
						#print 'Apagou o id %s' % apaga_origem
						print 'destino e %s' % destino
						
						if len(destino) < 7:
							if destino != '':

								apaga_destino = "DELETE FROM pabx_rt_calls WHERE ChannelState = 9 AND CallerIDNum = %s" %destino
								#print apaga_destino
								apaga_destino = c.execute(apaga_destino)
								connection.commit()
								#print 'Apagou o id %s' % apaga_destino
						else: 
							pass

						zz = funcao.checa_status_id(str(unico))
						print 'zz e %s e unico e %s' %(zz,unico)

						if zz != None:
							atualiza_ring = """UPDATE pabx_rt_calls SET Duration = '%s' WHERE Uniqueid = '%s' AND ChannelStateDesc = 'Ring' """ % (Duration,unico)
							#print atualiza_ring
							atualiza_ring = c.execute(atualiza_ring)
							connection.commit()
							atualiza_ringing = """UPDATE pabx_rt_calls SET Duration = '%s' WHERE Uniqueid = '%s' AND ChannelStateDesc = 'Ringing' """ % (Duration,unico)
							#print atualiza_ringing
							atualiza_ringing = c.execute(atualiza_ringing)
							#print atualiza
							connection.commit()

						else:
							print 'inserindo......'
							SQL_INSERE = ("INSERT INTO pabx_rt_calls"
									"(Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
										AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId,controle)"
									"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)")

							DADOS = (canal,channelState,channelDesc,origem,CallerIDName,ConnectedLineNum,ConnectedLineName,\
									AccountCode,Context,destino,Priority,unico,dial,Duration,BridgeId)
							c.execute(SQL_INSERE, DADOS)
							connection.commit()


				if state == '6':
					print  'alterando o status para 6'

					sql = "UPDATE pabx_rt_calls SET ChannelState = 6, ChannelStateDesc = 'Up' WHERE Uniqueid = %s" % unico
					#print sql
					sql = c.execute(sql)
					sql = c.fetchone()
					connection.commit()
					atualiza_ring = """UPDATE pabx_rt_calls SET Duration = '%s' WHERE Uniqueid = '%s' AND ChannelStateDesc = 'Up' """ % (Duration,unico)
					#print atualiza_ring
					atualiza_ring = c.execute(atualiza_ring)
					connection.commit()
	except:
		pass

def main():

	canais_tmp.main()
	funcao.insere_ramal()
	funcao.upadate_status_ramal()
	canais_tmp.apaga_canais_RT()
	insere_chamada()

main()