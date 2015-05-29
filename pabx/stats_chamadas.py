# -*- coding: UTF-8 -*-
#!/usr/bin/env python


import MySQLdb
import funcoes as funcao
import channel_status as canais
import canais_tmp


## Conexão ao banco MySQL
connection = MySQLdb.connect(host='localhost', user='root', passwd='app2004', db='cdrport')
c = connection.cursor()

def insere_chamada():

	lista = int(len(canais.origem_unico))
	print lista


	contador = -1
	while  contador < len(canais.origem_unico):
		

			contador = contador +1
			print contador
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

			x = canais.uniqueid_existente(unico)
			x = x
			print  unico, state

			if state == '4' or '5':
				print  'alterando o status para 4'
				print x, unico
				if x == unico:
					print 'ja tem'

				else:
					try:
						print 'inserindo chamanda'
						
						apaga_origem = "DELETE FROM pabx_rt_calls WHERE ChannelState = 9 AND CallerIDNum = %s" %origem
						print apaga_origem
						apaga_origem = c.execute(apaga_origem)
						connection.commit()
						print 'Apagou o id %s' % apaga_origem
						apaga_destino = "DELETE FROM pabx_rt_calls WHERE ChannelState = 9 AND CallerIDNum = %s" %destino
						print apaga_destino
						apaga_destino = c.execute(apaga_destino)
						connection.commit()
						print 'Apagou o id %s' % apaga_destino

						SQL_INSERE = ("INSERT INTO pabx_rt_calls"
								"(Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
									AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId,controle)"
								"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)")

						DADOS = (canal,channelState,channelDesc,origem,CallerIDName,ConnectedLineNum,ConnectedLineName,\
								AccountCode,Context,destino,Priority,unico,dial,Duration,BridgeId)
						c.execute(SQL_INSERE, DADOS)
						connection.commit()

					except:
						pass

			if state == '6':
				print  'alterando o status para 6'

				sql = "UPDATE pabx_rt_calls SET ChannelState = 6, ChannelStateDesc = 'Up' WHERE Uniqueid = %s" % unico
				print sql
				sql = c.execute(sql)
				sql = c.fetchone()
				connection.commit()


def main():

	canais_tmp.main()
	funcao.insere_ramal()
	canais_tmp.apaga_canais_RT()
	insere_chamada()

main()