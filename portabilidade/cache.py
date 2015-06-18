import sqlite3
import time
import datetime

# -*- coding: UTF-8 -*-
data_atual = datetime.datetime.now()



if not ('cache.s3db'):
        strsql = ("""
                create table cache (numero, csp)
            """)
        c.execute(strsql)

connection = sqlite3.connect('cache.s3db')
c = connection.cursor()
connection.text_factory = str

dados = [(55321,'CLARO S. A'),
        (55312,'CTBC CELULAR S.A'),
        (55301,'DATORA TELECOMUNICACOES LTDA'),
        (55130,'WKVE ASSESSORIA EM SERVICOS DE INFORMATICA E TELECOMUNICACOES LTDA')]


c.executemany('''INSERT INTO cache (numero, csp) VALUES(?, ?)''', dados)
connection.commit()