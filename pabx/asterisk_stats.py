# coding:utf-8

'''
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
main_url = 'http://sip.tofalando.com.br:8088/asterisk/rawman?'
#main_url = 'http://192.168.2.230:8088/rawman?'
cookie = ''


def stats_request(action=None):
    data = urllib.urlencode({'action': 'Login', 'username': 'root','secret': 'ZhVKlFXeCgTNyBr9lbIH',})
    #data = urllib.urlencode({'action': 'Login', 'username': 'asterisk','secret': 'senha',})
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


    # Aqui, colocamos os dados num arquivo temporÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬ ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rio, na memÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬ ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³ria.
    # Quebramos em linhas para podermos iterar...
    output = StringIO()
    #mydata = my_request(action='Login')
    output.writelines(response.read())
    lines = output.getvalue().splitlines()
    #output.close()
    #output = None

    # Criamos uma lista temporÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬ ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rio com nossas chaves e valores, para podermos
    # preencher nosso dicionÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬ ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rio
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
            if temp[1].strip() != '0000000':
                if mydict.has_key(temp[0]):
                    asterisk.append(mydict)
                    mydict = {}
                if temp[0].startswith('Status'):
                    temp[1] = temp[1][temp[1].rfind('(')+1:-1]
                mydict[temp[0]] = temp[1].strip()

    return asterisk
