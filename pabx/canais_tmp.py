# coding: utf-8
#!/usr/bin/env python
import MySQLdb
import channel_status as canais
import json
import globais
#import channel_status as canais

'''
CREATE TABLE `TMP_canais` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `Uniqueid` varchar(100) DEFAULT NULL,
  `CallerIDNum` varchar(100) DEFAULT NULL,
  `Exten` varchar(100) DEFAULT NULL,
  `ChannelStateDesc` varchar(10) DEFAULT NULL,
  `ChannelState` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Uniqueid` (`Uniqueid`)
) ENGINE=MEMORY AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
'''

## Conexão ao banco MySQL
connection = MySQLdb.connect(host=globais.host, user=globais.user, passwd=globais.password, db=globais.db)
c = connection.cursor()

id_morto = "SELECT Uniqueid FROM TMP_canais"
id_morto = c.execute(id_morto)
id_morto = c.fetchall()
id_morto = id_morto

id_morto_v = []

def insere_canais_tmp():

	'''
	Esta função insere no banco todos os novo Uniqueid's .
	'''

	try:

		contador = -1
		while canais.CallerIDNum and contador < len(canais.origem_unico):
			
			try:

				contador = contador + 1
				unico = canais.id_unico[contador]
				origem = canais.origem_unico[contador]
				destino = canais.destino_unico[contador]
				channel = canais.channelDESC_unico[contador]
				state = canais.channelSTATE_unico[contador]

				x = canais.uniqueid_existente(unico)
				x = x
				#print  unico, state

				if state == '4':
					print  'alterando o status para 4'

					if x == unico:
						pass
					else:
						#print '%s nao e igual a %s' % (unico,x)
						
						SQL_INSERE = ("INSERT INTO TMP_canais"
									"(Uniqueid,CallerIDNum,Exten,ChannelStateDesc,ChannelState)"
									"VALUES (%s,%s,%s,%s,%s)")
						DADOS = (unico,origem,destino,channel,state)
						c.execute(SQL_INSERE, DADOS)
						connection.commit()
						#print 'Inseriu novo..'
				elif state == '5':
					#print  'alterando o status para 5'

					if x == unico:
						pass
					else:
						print '%s nao e igual a %s' % (unico,x)
						
						SQL_INSERE = ("INSERT INTO TMP_canais"
									"(Uniqueid,CallerIDNum,Exten,ChannelStateDesc,ChannelState)"
									"VALUES (%s,%s,%s,%s,%s)")
						DADOS = (unico,origem,destino,channel,state)
						c.execute(SQL_INSERE, DADOS)
						connection.commit()
						#print 'Inseriu novo..'

				elif state == '0':
					#print  'alterando o status para 5'

					if x == unico:
						pass
					else:
						print '%s nao e igual a %s' % (unico,x)
						
						SQL_INSERE = ("INSERT INTO TMP_canais"
									"(Uniqueid,CallerIDNum,Exten,ChannelStateDesc,ChannelState)"
									"VALUES (%s,%s,%s,%s,%s)")
						DADOS = (unico,origem,destino,channel,state)
						c.execute(SQL_INSERE, DADOS)
						connection.commit()
						#print 'Inseriu novo..'

				if state == '6':
					#print  'alterando o status para 6'

					sql = "UPDATE TMP_canais SET ChannelState = 6, ChannelStateDesc = 'Up' WHERE Uniqueid = %s" % unico
					#print sql
					sql = c.execute(sql)
					sql = c.fetchone()
					connection.commit()



			except MySQLdb.IntegrityError as e:
				pass

			except IndexError as e:
				pass
	except:
		pass




def apaga_canais_tmp():
	'''
	Esta função remove do banco todos os Uniqueid's que não mais existem.
	'''


	sql = canais.validar_uniqueid()
	if sql == canais.id_unico:
		print 'ok'
	else:
		sql = "DELETE FROM TMP_canais WHERE id != 0 %s " % sql
		sql = c.execute(sql)
		connection.commit()
		print 'Apagou o id %s' % sql

def apaga_canais_RT():
	'''
	Esta função remove do banco todos os Uniqueid's que não mais existem na tabela pabx_rt_calls.
	'''

	sql = "DELETE FROM pabx_rt_calls WHERE ChannelState != 9 AND Uniqueid NOT IN (SELECT Uniqueid FROM TMP_canais)"
	sql = c.execute(sql)
	connection.commit()
	print 'Apagou o id %s' % sql

def main():

	'''
	Esta função é iniciada ao rodar este script
	'''
	try:
		
		apaga_canais_tmp()
		insere_canais_tmp()
	
	except:
		
		sql = "DELETE FROM TMP_canais"
		sql = c.execute(sql)
		connection.commit()
		print 'Apagou ligações mortas'
		
main()

