# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Template

from pabx.models import VwSipregs, rt_calls
from cdr.models import Info
from datetime import datetime, timedelta, time
import asterisk_stats as asterisk
import simplejson as json

'''
https://github.com/Star2Billing/cdr-stats/blob/master/cdr_stats/cdr/tasks.py
http://www.voip-info.org/wiki/view/show+channels
http://www.voip-info.org/wiki/view/channel+status
http://lists.digium.com/pipermail/asterisk-users/2012-February/270701.html
http://www.voip-info.org/wiki/view/Asterisk+cmd+SetAMAFlags
<status> values:
0 Channel is down and available
1 Channel is down, but reserved
2 Channel is off hook
3 Digits (or equivalent) have been dialed
4 Line is ringing
5 Remote end is ringing (Recebendo a chamada)
6 Line is up
7 Line is busy
'''

def pabx(request):


	exten = rt_calls.objects.all()
	#print exten
	info = Info.objects.values_list('ativo')
	info = str(info)[2]
	troncos = asterisk.stats_request('SIPshowregistry')
	ramais_sip = VwSipregs.objects.all()



	template = loader.get_template('mesa.html')
	context = RequestContext(request, {'info':info,'exten':exten, 'ramais_sip':ramais_sip, 'troncos':troncos})
	return HttpResponse(template.render(context))
	




