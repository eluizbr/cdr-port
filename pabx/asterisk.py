# coding:utf-8

'''
FILEDS: http://www.voip-info.org/wiki/view/show+channels
action=hangup&Channel=SIP/x7065558529-99a0
rawman?action=command&command=core%20show%20uptime
core show sysinfo
core show uptime
core show version
http://192.168.2.230:8088/asterisk/rawman?action=Status&Channel=SIP/400-00000077
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
#main_url = 'http://sip.tofalando.com.br:8088/asterisk/rawman?'
main_url = 'http://192.168.2.230:8088/asterisk/rawman?'
cookie = ''
 

def stats_request(action=None):
    #data = urllib.urlencode({'action': 'Login', 'username': 'root','secret': 'ZhVKlFXeCgTNyBr9lbIH',})
    data = urllib.urlencode({'action': 'Login', 'username': 'root','secret': 'senha',})
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
    data2 = data2.replace('%26', '&', 1).replace('%3D', '=', 1).replace('+', '%20', 3)
    url2 = main_url + data2
    req = urllib2.Request(url2)
    req.add_header('cookie', cookie)
    response = urllib2.urlopen(req)
    #print response.read()
    #return response.read()
 
 
    # Aqui, colocamos os dados num arquivo temporÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¡rio, na memÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â³ria.
    # Quebramos em linhas para podermos iterar...
    output = StringIO()
    #mydata = my_request(action='Login')
    output.writelines(response.read())
    lines = output.getvalue().splitlines()
    print lines
    #output.close()
    #output = None
 
    # Criamos uma lista temporÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¡rio com nossas chaves e valores, para podermos
    # preencher nosso dicionÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¡rio
    mydict = {}
    asterisk = []


    for z in asterisk:
        asterisk.append(z)


     
    print asterisk
stats_request('command&command=core show channels concise')


