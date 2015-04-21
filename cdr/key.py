# -*- coding: utf-8 -*-
# https://guevara2012.wordpress.com/2011/06/19/identificando-o-hardware-com-dmidecode-no-ubuntu/
# http://www.thegeekstuff.com/2008/11/how-to-get-hardware-information-on-linux-using-dmidecode-command/
# http://www.cyberciti.biz/tips/querying-dumping-bios-from-linux-command-prompt.html
# DETALHES = http://fibrevillage.com/sysadmin/34-dmidecode-examples-to-get-hardware-infomation
# dmidecode -t system
# dmidecode -s (strings)
# UUID : dmidecode -s system-uuid = 193E72FB-92CA-B14F-BC80-0317407F7DD7
# SERIAL NUMBER: dmidecode -s system-serial-number = Parallels-FB 72 3E 19 CA 92 4F B1 BC 80 03 17 40 7F 7D D7

# dmidecode 2.12

UUID : dmidecode -s system-uuid = 193E72FB-92CA-B14F-BC80-0317407F7DD7
SERIAL NUMBER: dmidecode -s system-serial-number = Parallels-FB 72 3E 19 CA 92 4F B1 BC 80 03 17 40 7F 7D D7
PROCESSOR: dmidecode -s processor-manufacturer = GenuineIntel
BIOS VERSION: dmidecode -s bios-version = 6.00
FREQUENCY PROCESSOR: dmidecode -s  processor-frequency = 2500 MHz
SYSTEM NAME: dmidecode -s system-product-name = Parallels Virtual Platform
MAC ADDREESS: cat /sys/class/net/eth?/address 

import MySQLdb
from datetime import datetime, timedelta, time
import os
import commands

## Conexão ao banco MySQL
connection = MySQLdb.connect(host='localhost', user='root', passwd='app2004', db='cdrport')
c = connection.cursor()
## Configurções padrão para data e hora
hoje = datetime.now()
proximo_mes = hoje + timedelta(days=31)



uuid = commands.getoutput('dmidecode -s system-uuid')
print uuid
system_number = commands.getoutput('dmidecode -s system-serial-number')
print system_number
system_name = commands.getoutput('dmidecode -s system-product-name')
print system_name
mac = commands.getoutput('cat /sys/class/net/eth?/address')
print mac
frequencia = commands.getoutput('dmidecode -s  processor-frequency')
print frequencia

SQL_INSERE = ("INSERT INTO info" 
            "(uuid, system_numer, system_name, mac, frequencia, data_ativacao, data_expira)" 
            "VALUES  (%s, %s, %s, %s, %s, %s)")
DADOS = (uuid, system_number, system_name, mac, frequencia, hoje, proximo_mes)

c.execute(SQL_INSERE, DADOS)

print 'O numero %s foi ADICIONADO'%(numero1)
print 'Operadora e %s, %s, %s, %s, %s, %s'%(DADOS)
connection.commit()

