# coding:utf-8
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO
 
import urllib2
import urllib
import json
 
myrequesturl = ''
main_url = 'http://sip.tofalando.com.br:8088/asterisk/rawman?'
cookie = ''
 
def my_request(action=None):
 
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
output.writelines(my_request(action='Login'))
lines = output.getvalue().splitlines()
 
# Criamos uma lista temporÃƒÂ¡rio com nossas chaves e valores, para podermos
# preencher nosso dicionÃƒÂ¡rio
mydict = {}
my_lst = []
 
for l in lines:
    temp = l.split(':')
    # if l.startswith('Uniqueid') or l.startswith('Extension'):
    if len(temp) > 1:
        if mydict.has_key(temp[0]):
            my_lst.append(mydict)
            mydict = {}
        mydict[temp[0]] = temp[1]
 
#print mydict
#print my_lst

