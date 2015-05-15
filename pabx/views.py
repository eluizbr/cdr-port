# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from cdr.models import cdr, DispositionPercent, Info, Cdrport,Config_Local
from cdr.models import  VwDayStats, VwMonthStats,VwLast10, VwOperadoras, VwStatsAnswered, VwStatsBusy, VwStatsNoanswer, VwRamais,\
                    VwDisposition, VwCdr, VwCidades, VwEstados
from pabx.models import VwSipregs,  Cel, rt_calls
from django.db.models import Sum, Count, Avg, Max, Min
from datetime import datetime, timedelta, time
from django.db.models import Q
from django.http import QueryDict
import asterisk_stats as asterisk
from django.core import serializers
import ari
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
	
	exten = asterisk.stats_request('CoreShowChannels')


	troncos = asterisk.stats_request('SIPshowregistry')
	ramais_sip = VwSipregs.objects.all()
	eventos =  Cel.objects.all()
	eventos_id =  Cel.objects.values_list('uniqueid')
	#print eventos_id


	template = loader.get_template('mesa.html')
	context = RequestContext(request, {'exten':exten, 'ramais_sip':ramais_sip, 'eventos':eventos, 'troncos':troncos})
	return HttpResponse(template.render(context))

	




