# -*- coding: UTF-8 -*-
#!/usr/bin/env python


import MySQLdb
import asterisk_stats as asterisk
import channel_status as canais
import random
import globais


## Conexão ao banco MySQL
connection = MySQLdb.connect(host=globais.host, user=globais.user, passwd=globais.password, db=globais.db)
c = connection.cursor()



def insere_ramal():

	'''
	Esta função insere o ramal que não esta em uso ou não existe na tabela pabx_rt_calls.
	Uso:
		var = insere_ramal(ramal)
	'''


	pega_ramal = "SELECT name FROM vw_sipregs WHERE name not in (SELECT CallerIDNum FROM pabx_rt_calls)" 
	pega_ramal = c.execute(pega_ramal)
	pega_ramal = c.fetchall()
	
	for ramal_v in pega_ramal:
		ramal_v = str(ramal_v[0])

		ipaddr = "SELECT ipaddr FROM vw_sipregs WHERE name = " + str(ramal_v)
		ipaddr = c.execute(ipaddr)
		ipaddr = c.fetchone()[0]
		#print ipaddr

		lastms = "SELECT lastms FROM vw_sipregs WHERE name = " + str(ramal_v)
		lastms = c.execute(lastms)
		lastms = c.fetchone()[0]
		#print lastms
		numero = random.randint(7500000000.000, 8500000000.000)
		#print numero
		#print ramal_v, ipaddr, lastms

		SQL_INSERE = ("INSERT INTO pabx_rt_calls"
					"(CallerIDNum,ChannelState,ChannelStateDesc,Uniqueid,Duration,controle,ipaddr,lastms)"
					"VALUES (%s,9,'Dead',%s,'00:00:00',8,%s,%s)")

		DADOS = (ramal_v,numero,ipaddr,lastms)
		c.execute(SQL_INSERE, DADOS)
		connection.commit()	


def checa_status_ramal(ramal):


	pega_ramal = "SELECT CallerIDNum FROM pabx_rt_calls WHERE CallerIDNum = %s" % ramal
	#print pega_ramal
	pega_ramal = c.execute(pega_ramal)
	pega_ramal = c.fetchone()[0]
	#print pega_ramal
	#print canais.origem_unico
	contador = -1
	try:
		while canais.CallerIDNum and contador < len(canais.origem_unico):
			
			try:
				contador = contador + 1
				callerid = canais.origem_unico[contador]
				#print callerid

				if callerid == pega_ramal:
					#print '%s e igual a %s' % (callerid,pega_ramal)
					ramal = altera_status_ramal(callerid,9)
					#print ramal
				else:
					#print '%s e diferente %s' % (callerid,pega_ramal)
					pass

			except IndexError as e:
				pass
	except:
		#print 'Nenhuma ligação no momento'
		ramal = altera_status_ramal(pega_ramal,8)
		#print ramal


def altera_status_ramal(ramal,controle):



	atualiza_ramal = "UPDATE pabx_rt_calls SET controle = %s WHERE CallerIDNum = %s" % (controle,ramal)
	#print atualiza_ramal
	atualiza_ramal = c.execute(atualiza_ramal)
	atualiza_ramal = c.fetchone()
	connection.commit()
	#print atualiza_ramal

def consulta_ramal(ramal):

	try:
		consulta = "SELECT Uniqueid FROM TMP_canais WHERE CallerIDNum = %s" % ramal
		#print consulta
		consulta = c.execute(consulta)
		consulta = c.fetchone()[0]
		#print consulta

		if consulta == canais.uniqueid_existente(consulta):
			#print 'ramal %s esta em ligacao' %ramal
			pass

	except:
		print 'ramal %s esta diaponivel' %ramal


def checa_status_id(uniqueid=None):

	
	sql = "SELECT Uniqueid FROM pabx_rt_calls WHERE Uniqueid = %s" % (uniqueid)
	print sql
	sql = c.execute(sql)
	sql = c.fetchone()
	#connection.commit()
	print sql
	return sql

#checa_status_id('1432928438.166091')
