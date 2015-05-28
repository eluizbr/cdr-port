# -*- coding: UTF-8 -*-
#!/usr/bin/env python


import MySQLdb
import funcoes as funcao
import channel_status as canais
import canais_tmp
import json

## Conexão ao banco MySQL
connection = MySQLdb.connect(host='localhost', user='root', passwd='app2004', db='cdrport')
c = connection.cursor()



def insere_chamada(ramal):

	canais_tmp.apaga_canais_RT()
	id_unico = canais.uniqueid_ramal(ramal)
	caller = canais.Ramais(ramal)
	origem = caller.origem(ramal)
	destino = caller.destino(ramal)
	#print 'Ramal %s ligando para %s' % (origem,destino)

	del_ring = "DELETE CallerIDNum FROM pabx_rt_calls WHERE CallerIDNum = %s AND Uniqueid = %s" % (origem,id_unico)
	#print del_ring
	#del_ring = c.execute(del_ring)
	#connection.commit()

	del_ringing = "DELETE CallerIDNum FROM pabx_rt_calls WHERE CallerIDNum = %s AND Uniqueid = %s" % (destino,id_unico)
	#print del_ringing
	#del_ringing = c.execute(del_ringing)
	#connection.commit()
	try:
		SQL_INSERE = ("INSERT INTO pabx_rt_calls"
				"(Channel,ChannelState,ChannelStateDesc,CallerIDNum,CallerIDName,ConnectedLineNum,ConnectedLineName,\
					AccountCode,Context,Exten,Priority,Uniqueid,Application,Duration,BridgeId,controle)"
				"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)")

		DADOS = (canais.Channel,canais.ChannelState,canais.ChannelStateDesc,canais.CallerIDNum,canais.CallerIDName,canais.ConnectedLineNum,canais.ConnectedLineName,\
				canais.AccountCode,canais.Context,canais.Exten,canais.Priority,canais.Uniqueid,canais.Application,canais.Duration,canais.BridgeId)
		c.execute(SQL_INSERE, DADOS)
		connection.commit()
	except:
		print 'nao existe chamadas'
		print canais.uniqueid_existente(canais.id_unico)

insere_chamada(300)



def main():

	canais_tmp.main()


	funcao.insere_ramal(301)

main()