# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from cdr.models import cdr, DispositionPercent, Info, Cdrport,Config_Local
from cdr.models import  VwDayStats, VwMonthStats,VwLast10, VwOperadoras, VwStatsAnswered, VwStatsBusy, VwStatsNoanswer, VwRamais,\
                    VwDisposition, VwCdr, VwCidades, VwEstados
from pabx.models import VwSipregs,  Cel
from django.db.models import Sum, Count, Avg, Max, Min
from datetime import datetime, timedelta, time
from django.db.models import Q
from django.http import QueryDict
import asterisk_stats as asterisk
import json

'''
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
	
	exten = asterisk.stats_request('CoreShowChannels')
	#x = json.dumps(exten, indent=1)
	#print x

	ramais_sip = VwSipregs.objects.all()
	sip = VwSipregs.objects.all()

	eventos =  Cel.objects.all()
	#print eventos
	#uniqueid = exten[0]["UniqueID"]
	#d = dict(uniqueid=uniqueid)
	#print d
	'''
	sipx = '400'
	extension = exten["Extension"]
	print extension
	channel = exten["Channel"]
	context = exten["Context"]
	channelstatedesc = exten["ChannelStateDesc"]
	aplication = exten["Application"]
	duration = exten["Duration"]
	channelstate = exten["ChannelState"]
	uniqueid = exten["UniqueID"]
	
	d = dict(extension=extension, channel=channel, context=context, aplication=aplication,
			channelstatedesc=channelstatedesc, duration=duration, channelstate=channelstate, uniqueid=uniqueid)
	print d
	'''

	template = loader.get_template('mesa.html')
	context = RequestContext(request, {'exten':exten, 'ramais_sip':ramais_sip, 'eventos':eventos})
	return HttpResponse(template.render(context))

	




