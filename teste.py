# -*- coding: UTF-8 -*-
import sys

numero = str(sys.argv[1])
numero = numero[2:]
print numero



'''
numero = numero[::-1]

if len(numero) == 8:
	print numero
	print 'Local'

elif len(numero) == 9:
	print numero
	print 'Local'

elif len(numero) == 10:
	print 'LDN 8'
	print numero[:8]
	print numero[::-1]

elif len(numero) == 11:
	print numero
	print 'LDN Movel SP'

elif len(numero) < 8:
	print numero
	print 'Ramal'

else:
	print 'nao'

'''