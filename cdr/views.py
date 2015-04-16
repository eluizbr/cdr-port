from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from .models import cdr, DispositionPercent, Stats_ANSWERED, Stats_NOANSWER, Stats_BUSY
from .models import VwDayStats, VwMonthStats,VwLast10, VwOperadoras, VwStatsAnswered, VwStatsBusy, VwStatsNoanswer, VwRamais,\
                    VwDisposition
from django.db.models import Sum, Count, Avg, Max, Min
from datetime import datetime, timedelta, time
from django.db.models import Q

def index(request):
    perc = DispositionPercent.objects.values_list('disposition', 'valor', 'perc')
    total = DispositionPercent.objects.aggregate(Sum('valor'))['valor__sum']
    stats_AN = VwStatsAnswered.objects.values_list('dia', 'semana', 'mes')
    stats_NO = VwStatsNoanswer.objects.values_list('dia', 'semana', 'mes')
    stats_BU = VwStatsBusy.objects.values_list('dia', 'semana', 'mes')
    ultimo = VwLast10.objects.values_list('numero','calldate','billsec')
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

    ultimo = VwLast10.objects.values_list('numero','operadora','tipo','calldate', 'disposition' ,'billsec')
    resultado = cdr.objects.values_list('dst', 'src', 'calldate', 'disposition', 'duration', 'billsec').order_by('-calldate')
    src = VwRamais.objects.all()
    numero = cdr.objects.all()
    calldate = cdr.objects.all()
    disposition = VwDisposition.objects.all()

    paginator = Paginator(resultado, 15)

    page = request.GET.get('page', '1')

    try:
        resultado_1 = paginator.page(page)
    except(EmptyPage, InvalidPage):
        resultado_1 = paginator.page(paginator.num_pages)

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
    '''
    if tronco:
        query &=Q(src__icontains=src_f)
    if numero:
        query &=Q(numero__startswith=numero_f)
    if operadora:
        query &=Q(operadora__icontains=operadora_f)
    if csp:
        query &=Q(csp__icontains=csp_f)
    if cidade:
        query &=Q(cidade__icontains=cidade_f)
    if estado:
        query &=Q(estado__icontains=estado_f)
    if disposition:
        query &=Q(disposition__icontains=disposition_f)
    if tipo:
        query &=Q(tipo__icontains=tipo_f)
    if portado:
        query &=Q(portado__icontains=portado_f)
    if calldate:

        query &=Q(calldate__range=(calldate1,calldate2))
    if ddd:
        query &=Q(ddd__icontains=ddd_f)
    '''


    results = cdr.objects.filter(query).order_by('-calldate')

    template = loader.get_template('cdr.html')
    context = RequestContext(request, {'ultimo':ultimo, 'resultado_1':resultado_1 ,'results':results, 'src':src, 'numero':numero,
                                        'calldate':calldate, 'hoje':hoje, 'ontem':ontem, 'disposition':disposition, })
    return HttpResponse(template.render(context))
    
