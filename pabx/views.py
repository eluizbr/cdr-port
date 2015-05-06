# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from cdr.models import cdr, DispositionPercent, Info, Cdrport,Config_Local
from cdr.models import VwDayStats, VwMonthStats,VwLast10, VwOperadoras, VwStatsAnswered, VwStatsBusy, VwStatsNoanswer, VwRamais,\
                    VwDisposition, VwCdr, VwCidades, VwEstados
from django.db.models import Sum, Count, Avg, Max, Min
from datetime import datetime, timedelta, time
from django.db.models import Q
from django.http import QueryDict
import asterisk_stats as asterisk
from django.core.cache import cache


def pabx(request):
	
	#ramais_sip  = asterisk.sip
	exten = asterisk.stats_request('CoreShowChannels')
	print exten
	ramais_sip = asterisk.stats_request('SIPpeers')
	trunk = asterisk.stats_request('SIPshowregistry')
	info = Info.objects.values_list('ativo')
	info = str(info)[2]
	perc = DispositionPercent.objects.values_list('disposition', 'valor', 'perc')
	total = DispositionPercent.objects.aggregate(Sum('valor'))['valor__sum']
	stats_AN = VwStatsAnswered.objects.values_list('dia', 'semana', 'mes')
	stats_NO = VwStatsNoanswer.objects.values_list('dia', 'semana', 'mes')
	stats_BU = VwStatsBusy.objects.values_list('dia', 'semana', 'mes')
	ultimo = VwLast10.objects.values_list('dst','operadora', 'tipo','calldate','cidade', 'estado', 'portado')
	byDay = VwDayStats.objects.values_list('dia', 'mes', 'total')
	byMonth = VwMonthStats.objects.values_list('mes', 'total')
	operadora = VwOperadoras.objects.values_list('operadora', 'total')
	cidade = VwCidades.objects.values_list('cidade').count()
	portados_s = Cdrport.objects.filter(portado='Sim').count()
	portados_n = Cdrport.objects.filter(portado='Nao').count()
	template = loader.get_template('pabx.html')
	context = RequestContext(request, {'exten':exten, 'ramais_sip':ramais_sip, 'trunk':trunk, 'info':info, 'perc': perc, 'total': total, 'stats_AN':stats_AN, 'stats_NO':stats_NO,'cidade':cidade,'portados_s':portados_s,
								    	'portados_n':portados_n,'stats_BU':stats_BU, 'ultimo':ultimo, 'byDay':byDay, 'byMonth':byMonth, 'operadora':operadora })
	return HttpResponse(template.render(context))

	




