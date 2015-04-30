#!/usr/bin/python

# Referencia: https://github.com/rdegges/pyst2
#agi.appexec('Dial','SIP/%s,60,Tt' %x)

import asterisk_consulta as port
from asterisk.agi import *

'''
; 10 Digitos
exten => _XXXXXXXXXX,1,Answer()
exten => _XXXXXXXXXX,n,AGI(/root/executa.py,${EXTEN})
exten => _XXXXXXXXXX,n,NoOp(${NUMERO})
exten => _XXXXXXXXXX,n,Dial(SIP/${NUMERO})
exten => _XXXXXXXXXX,n,Dial(SIP/GSM01/0${NUMERO:3})
exten => _XXXXXXXXXX,n,Hangup
'''

agi = AGI()
x = port.consulta_numero(sys.argv[1])
canal = agi.env['agi_channel']
agi.appexec('Set','NUMERO=%s' %x)
agi.set_variable('NUMERO', '%s' %x)