# -*- coding: UTF-8 -*-
#!/usr/bin/env python


'''


curl https://www.cloudflare.com/api_json.html \
  -d 'a=rec_new' \
  -d 'tkn=8afbe6dea02407989af4dd4c97bb6e25' \
  -d 'email=sample@example.com' \
  -d 'z=example.com' \
  -d 'type=A' \
  -d 'name=sub' \
  -d 'content=1.2.3.4'

'''


"""
Pull out statistics from CloudFlare, parse it
and output return a string with the traffic breakdown
of today

"""

import urllib
import urllib2
import json


URL = "https://www.cloudflare.com/api_json.html"
API_KEY = "8afbe6dea02407989af4dd4c97bb6e25"
SITE = "tofalando.com.br"
MAIL = "eluizbr@gmail.com"
NOME = "beta1"

PARAMETERS = {
    'a': 'rec_new',
    'tkn': API_KEY,
    'email': MAIL,
    'z': SITE,
    'type': 'A',
    'name': NOME,
    'content': '177.52.104.54'
}

