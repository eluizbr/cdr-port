# coding:utf-8
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO
 
import urllib2
import urllib
import json
import re
 
myrequesturl = ''
main_url = 'http://sip.tofalando.com.br:8088/asterisk/rawman?'
cookie = ''
 

def sip_request(action=None):
 
    data = urllib.urlencode({'action': action, 'username': 'root','secret': 88285069,})
    myrequesturlurl = main_url + data
    # print myrequesturlurl
    req = urllib2.Request(myrequesturlurl)
    response = urllib2.urlopen(req)
    cookie = response.headers.get('Set-Cookie')
    # print cookie
    d = response.read()
 
    #Depois de autenticado
    action = 'SIPpeers'
    data2 = urllib.urlencode({'action': action, })
    url2 = main_url + data2
    req = urllib2.Request(url2)
    req.add_header('cookie', cookie)
    response = urllib2.urlopen(req)
    # print response.read()
    return response.read()
 
 
# Aqui, colocamos os dados num arquivo temporÃƒÂ¡rio, na memÃƒÂ³ria.
# Quebramos em linhas para podermos iterar...
output = StringIO()
#mydata = my_request(action='Login')
output.writelines(sip_request(action='Login'))
lines = output.getvalue().splitlines()
output.close()
output = None
 
# Criamos uma lista temporÃƒÂ¡rio com nossas chaves e valores, para podermos
# preencher nosso dicionÃƒÂ¡rio
mydict = {}
sip = []
 
for l in lines:
    temp = l.split(':')
    # if l.startswith('Uniqueid') or l.startswith('Extension'):
    if len(temp) > 1:
        if mydict.has_key(temp[0]):
            sip.append(mydict)
            mydict = {}
        mydict[temp[0]] = temp[1]

#for item in sip:
 #   return item['ObjectName'], item['Status'], item['IPaddress'], item['IPport']

#print mydict
#print sip

def exten_request(action=None):
    

    data = urllib.urlencode({'action': action, 'username': 'root','secret': 88285069,})
    myrequesturlurl = main_url + data
    # print myrequesturlurl
    req = urllib2.Request(myrequesturlurl)
    response = urllib2.urlopen(req)
    cookie = response.headers.get('Set-Cookie')
    # print cookie
    d = response.read()
 
    #Depois de autenticado
    action = 'CoreShowChannels'
    data2 = urllib.urlencode({'action': action, })
    url2 = main_url + data2
    req = urllib2.Request(url2)
    req.add_header('cookie', cookie)
    response = urllib2.urlopen(req)
    # print response.read()
    return response.read()
 
 
# Aqui, colocamos os dados num arquivo temporÃƒÂ¡rio, na memÃƒÂ³ria.
# Quebramos em linhas para podermos iterar...
out_exten = StringIO()
#mydata = my_request(action='Login')
out_exten.writelines(exten_request(action='Login'))
lines = out_exten.getvalue().splitlines()
out_exten.close()
out_exten = None

 
# Criamos uma lista temporÃƒÂ¡rio com nossas chaves e valores, para podermos
# preencher nosso dicionÃƒÂ¡rio
mydict = {}
exten = []
 
for l in lines:
    # Se for duration, aí quebramos a string de outra forma ;)
    if l.startswith('Duration'):
        temp = re.split('\s+', l)
        temp[0] = temp[0][:-1]
    else:
        temp = l.split(':')

    if len(temp) > 1:
        if mydict.has_key(temp[0]):
            exten.append(mydict)
            mydict = {}
        mydict[temp[0]] = temp[1]



def trunk_request(action=None):
    
    data = urllib.urlencode({'action': action, 'username': 'root','secret': 88285069,})
    myrequesturlurl = main_url + data
    # print myrequesturlurl
    req = urllib2.Request(myrequesturlurl)
    response = urllib2.urlopen(req)
    cookie = response.headers.get('Set-Cookie')
    # print cookie
    d = response.read()
 
    #Depois de autenticado
    action = 'SIPshowregistry'
    data2 = urllib.urlencode({'action': action, })
    url2 = main_url + data2
    req = urllib2.Request(url2)
    req.add_header('cookie', cookie)
    response = urllib2.urlopen(req)
    # print response.read()
    return response.read()
 
 
# Aqui, colocamos os dados num arquivo temporÃƒÂ¡rio, na memÃƒÂ³ria.
# Quebramos em linhas para podermos iterar...
output = StringIO()
#mydata = my_request(action='Login')
output.writelines(trunk_request(action='Login'))
lines = output.getvalue().splitlines()
output.close()
output = None
 
# Criamos uma lista temporÃƒÂ¡rio com nossas chaves e valores, para podermos
# preencher nosso dicionÃƒÂ¡rio
mydict = {}
trunk = []
 
for l in lines:
    # Se for duration, aí quebramos a string de outra forma ;)
    if l.startswith('Duration'):
        temp = re.split('\s+', l)
        temp[0] = temp[0][:-1]
    else:
        temp = l.split(':')

    if len(temp) > 1:
        if mydict.has_key(temp[0]):
            trunk.append(mydict)
            mydict = {}
        mydict[temp[0]] = temp[1]

