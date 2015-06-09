# -*- coding: UTF-8 -*-

import MySQLdb
import random


## Conexão ao banco MySQL
connection = MySQLdb.connect(host=globais.host, user=globais.user, passwd=globais.password, db=globais.db)
c = connection.cursor()

"""
PF/PJ
Nome
Email
Senha
Endereço
Cidade
Estado
CEP
Dominio
CNPJ
CPF
IP_ASTERISK
COD_CLIENTE
"""


