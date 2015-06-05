# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import sys
import os
import random
from socket import gethostname, gethostbyname 

# Copyright (C) 2014 CDR-port
# cdr-port@cdr-port.net

def gerar_senha():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pw_length = 12
    senha = ""

    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        senha = senha + alphabet[next_index]
    return senha

# Config Global
#IP = gethostbyname(gethostname())
#USUARIO = str(sys.argv[1])
#DIRETORIO = '/tmp/%s' %USUARIO
#BRANCH = 'master'
DB_PASSWORD = gerar_senha()

print DB_PASSWORD

#Instalando CDR-port

#os.makedirs(DIRETORIO)





