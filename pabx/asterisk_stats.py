# coding:utf-8

'''
core show sysinfo
core show uptime
core show version
'''


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
 

def stats_request(action=None):
    data = urllib.urlencode({'action': 'Login', 'username': 'root','secret': 88285069,})
    myrequesturlurl = main_url + data
    #print myrequesturlurl
    req = urllib2.Request(myrequesturlurl)
    response = urllib2.urlopen(req)
    cookie = response.headers.get('Set-Cookie')
    #print cookie
    d = response.read()
 
    #Depois de autenticado
    # action = 'asteriskpeers'
    data2 = urllib.urlencode({'action': action, })
    url2 = main_url + data2
    req = urllib2.Request(url2)
    req.add_header('cookie', cookie)
    response = urllib2.urlopen(req)
    #print response.read()
    #return response.read()
 
 
    # Aqui, colocamos os dados num arquivo temporÃƒÆ’Ã‚Â¡rio, na memÃƒÆ’Ã‚Â³ria.
    # Quebramos em linhas para podermos iterar...
    output = StringIO()
    #mydata = my_request(action='Login')
    output.writelines(response.read())
    lines = output.getvalue().splitlines()
    output.close()
    output = None
 
    # Criamos uma lista temporÃƒÆ’Ã‚Â¡rio com nossas chaves e valores, para podermos
    # preencher nosso dicionÃƒÆ’Ã‚Â¡rio
    mydict = {}
    asterisk = []
 
    for l in lines:
        temp = l.split(':')
        if l.startswith('Duration'):
             temp = re.split('\s+', l)
             temp[0] = temp[0][:-1]
        else:
             temp = l.split(':')
        
        
        if len(temp) > 1:
            if mydict.has_key(temp[0]):
                asterisk.append(mydict)
                mydict = {}
            mydict[temp[0]] = temp[1]
     
    return asterisk
