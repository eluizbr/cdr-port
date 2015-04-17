from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from .models import cdr, DispositionPercent, Stats_ANSWERED, Stats_NOANSWER, Stats_BUSY
from .models import VwDayStats, VwMonthStats,VwLast10, VwOperadoras, VwStatsAnswered, VwStatsBusy, VwStatsNoanswer, VwRamais,\
                    VwDisposition, VwCdr
from django.db.models import Sum, Count, Avg, Max, Min
from datetime import datetime, timedelta, time
from django.db.models import Q

def index(request):
    perc = DispositionPercent.objects.values_list('disposition', 'valor', 'perc')
    total = DispositionPercent.objects.aggregate(Sum('valor'))['valor__sum']
    stats_AN = VwStatsAnswered.objects.values_list('dia', 'semana', 'mes')
    stats_NO = VwStatsNoanswer.objects.values_list('dia', 'semana', 'mes')
    stats_BU = VwStatsBusy.objects.values_list('dia', 'semana', 'mes')
    ultimo = VwLast10.objects.values_list('numero','operadora', 'tipo','calldate','billsec')
    byDay = VwDayStats.objects.values_list('dia', 'mes', 'total')
    byMonth = VwMonthStats.objects.values_list('mes', 'total')
    operadora = VwOperadoras.objects.values_list('operadora', 'total')
    template = loader.get_template('index.html')
    context = RequestContext(request, {'perc': perc, 'total': total, 'stats_AN':stats_AN, 'stats_NO':stats_NO,
								    	'stats_BU':stats_BU, 'ultimo':ultimo, 'byDay':byDay, 'byMonth':byMonth, 'operadora':operadora })
    return HttpResponse(template.render(context))


def time_line(request):
    
    hora = datetime.now()
    hoje = hora.strftime("%Y-%m-%dT23:59:59") 
    ontem = hora - timedelta(days=1)
    ontem = ontem.strftime("%Y-%m-%dT00:00:00")

    byDay = VwDayStats.objects.values_list('dia', 'mes', 'total')
    byMonth = VwMonthStats.objects.values_list('mes', 'total')
    ultimo = VwLast10.objects.values_list('numero','operadora','tipo','calldate', 'disposition' ,'billsec')
    resultado = VwCdr.objects.values_list('dst', 'src', 'calldate', 'disposition', 'duration', 'billsec').order_by('-calldate')
    src = VwRamais.objects.all()
    numero = VwCdr.objects.values_list('dst', 'src', 'calldate', 'disposition', 'duration', 'billsec')
    calldate = VwCdr.objects.values_list('dst', 'src', 'calldate', 'disposition', 'duration', 'billsec')
    disposition = VwDisposition.objects.all()


    numero_f = request.GET.get('numero', "")
    src_f = request.GET.get('src', "0")
    calldate1 = request.GET.get('calldate1', ontem)
    calldate2 = request.GET.get('calldate2', hoje)
    disposition_f = request.GET.get('disposition', "")

    query = Q()

    if numero:
        query &=Q(dst__startswith=numero_f)
    if src:
        query &=Q(src__icontains=src_f)
    if calldate:
        query &=Q(calldate__range=(calldate1,calldate2))
    if disposition:
        query &=Q(disposition__icontains=disposition_f)


    results = VwCdr.objects.filter(query).order_by('-calldate')

    paginator = Paginator(results, 25)
    page = request.GET.get('page', '1')
  
    try:
        resultado_1 = paginator.page(page)
    except PageNotAnInteger:
        resultado_1 = paginator.page(1)
    except (EmptyPage):
        resultado_1 = paginator.page(paginator.num_pages)

    url = "numero=%s&src=%s&calldate1=%s&calldate2=%s&disposition=%s"\
            % (numero_f, src_f, calldate1, calldate2, disposition_f)

    tempo_medio = results.aggregate(Avg('billsec'))['billsec__avg']
    tempo_medio = str(timedelta(seconds=tempo_medio))[:-7]
    tempo = results.aggregate(Sum('billsec'))['billsec__sum']
    #tempo = str(timedelta(seconds=tempo))
    print tempo
    periodo_dia_1 = calldate1[8:10]
    periodo_dia_2 = calldate2[8:10]
    periodo_mes_1 = calldate1[5:7]
    periodo_mes_2 = calldate2[5:7]
    total = results.aggregate(Count('src'))['src__count']
   # beta = results.aggregate(Count('disposition')).filter('ANSWERED')['disposition__count']
   # print beta

    template = loader.get_template('cdr.html')
    context = RequestContext(request, {'byDay':byDay, 'byMonth':byMonth, 'ultimo':ultimo, 'resultado_1':resultado_1 ,'results':results,
                                        'src':src, 'src_f':src_f ,'numero':numero, 'calldate':calldate, 'hoje':hoje, 'ontem':ontem, 
                                        'disposition':disposition, 'url':url, 'tempo_medio':tempo_medio, 'tempo':tempo, 'periodo_dia_1':periodo_dia_1,
                                        'periodo_dia_2':periodo_dia_2, 'periodo_mes_1':periodo_mes_1, 'periodo_mes_2':periodo_mes_2,
                                        'total':total })
    return HttpResponse(template.render(context))
    
