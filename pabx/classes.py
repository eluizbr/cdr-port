# -*- coding: UTF-8 -*-
#!/usr/bin/env python


import MySQLdb
import asterisk_stats as asterisk
import channel_status_18 as canais
import json
import random



## Conexão ao banco MySQL
connection = MySQLdb.connect(host='localhost', user='root', passwd='app2004', db='cdrport')
c = connection.cursor()

class Ramais:
	'''
	Esta classe, trata como esta o status atual do ramal. Ela trabalha quando 
	ramal esta em Stand By, e quando esta em ligação.
	
	'''

	def __init__(self,ramal):
		'''
		Esta função insere o ramal no MySQL quando ele incia uma ligação. Alterando seu status:
		Controle: 8 - Ramal em Stand By, 9 - Ramal em reservar (em ligação)
		'''

		self.ramal = ramal




	def insere_ramal(self):

		pega_ramal = "SELECT name FROM vw_sipregs WHERE name not in (SELECT CallerIDNum FROM pabx_rt_calls) ORDER BY convert(name,unsigned)"
		#print pega_ramal
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


	def checa_status_ramal(self,ramal):

		self.ramal = ramal

		pega_ramal = "SELECT CallerIDNum FROM pabx_rt_calls WHERE CallerIDNum = %s" % ramal
		#print pega_ramal
		pega_ramal = c.execute(pega_ramal)
		pega_ramal = c.fetchone()[0]
		#print pega_ramal

		contador = -1
		while canais.CallerIDNum and contador < len(canais.caller_unico):
			
			try:
				contador = contador + 1
				callerid = canais.caller_unico[contador]
				#print callerid

				if callerid == pega_ramal:
					print '%s e igual a %s' % (callerid,pega_ramal)
				else:
					print '%s e diferente %s' % (callerid,pega_ramal)


			except IndexError as e:
				pass



	def altera_status_ramal(self,ramal):

		self.ramal = ramal

		atualiza_ramal = "UPDATE pabx_rt_calls SET controle = %s WHERE CallerIDNum = %s" % (controle,ramal)
		print atualiza_ramal
		atualiza_ramal = c.execute(atualiza_ramal)
		atualiza_ramal = c.fetchone()[0]
		print type(atualiza_ramal)
		#print atualiza_ramal

		if atualiza_ramal == '5':
			print 'ramal é %s' % self.ramal
		else:

			print 'nada'



#ramal_400 = Ramais(300)
#status = ramal_400.checa_status_ramal(300)

'''
contador = -1
while canais.Uniqueid and contador < len(canais.id_unico):
	
	try:
		contador = contador + 1
		id = canais.id_unico[contador]
		print id

	except IndexError as e:
		pass	


		if pega_ramal == 5:
			print 'ramal é %s' % self.ramal
		
		else:

			print 'ramal %s tem status %s ' %(self.ramal, pega_ramal)

'''