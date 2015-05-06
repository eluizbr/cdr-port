import asterisk.manager
import sys

manager = asterisk.manager.Manager()


manager.connect('sip.tofalando.com.br')
manager.login('root', '88285069')

# get a status report
response = manager.status()
print(response)


response = manager.sippeers()


print(response.data)



manager.close()