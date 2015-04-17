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
    tipo = VwCdr.objects.values_list('tipo')
    operadora = VwOperadoras.objects.all()
    pagina = 20,30,50,100

    
    numero_f = request.GET.get('numero', "")
    src_f = request.GET.get('src', "0")
    calldate1 = request.GET.get('calldate1', ontem)
    calldate2 = request.GET.get('calldate2', hoje)
    disposition_f = request.GET.get('disposition', "")
    paginas_f = request.GET.get('pagina', "")
    tipo_f = request.GET.get('tipo', "")
    operadora_f = request.GET.get('operadora', "")

    if paginas_f == '':
        paginas_f = 15
    else:
        paginas_f = paginas_f

    query = Q()

    if numero:
        query &=Q(dst__startswith=numero_f)
    if src:
        query &=Q(src__icontains=src_f)
    if calldate:
        query &=Q(calldate__range=(calldate1,calldate2))
    if disposition:
        query &=Q(disposition__icontains=disposition_f)
    if tipo:
        query &=Q(tipo__icontains=tipo_f)
    if operadora:
        query &=Q(operadora__icontains=operadora_f)


    results = VwCdr.objects.filter(query).order_by('-calldate')

    url = "numero=%s&src=%s&calldate1=%s&calldate2=%s&disposition=%s&pagina=%s&tipo=%s&operadora=%s"\
        % (numero_f, src_f, calldate1, calldate2, disposition_f, paginas_f, tipo_f, operadora_f)

    tempo_medio = results.aggregate(Avg('billsec'))['billsec__avg']
    tempo_medio = str(timedelta(seconds=tempo_medio))[:-7]
    tempo_maior = results.aggregate(Max('billsec'))['billsec__max']
    tempo_menor = results.aggregate(Min('billsec'))['billsec__min']
    print tempo_menor
    tempo = results.aggregate(Sum('billsec'))['billsec__sum']
    if tempo == None:
        tempo = 0
    else:
        tempo = int(tempo)
        tempo = timedelta(seconds=tempo)
    periodo_dia_1 = calldate1[8:10]
    periodo_dia_2 = calldate2[8:10]
    periodo_mes_1 = calldate1[5:7]
    periodo_mes_2 = calldate2[5:7]
    total = results.aggregate(Count('src'))['src__count']

    ### SQL personalizado
    from django.db import connection
    cursor = connection.cursor()
    
    if operadora_f == '':


        atendeu = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'ANSWERED' AND src=%s AND tipo='%s'""" % (src_f, tipo_f)
        atendeu = cursor.execute(atendeu)
        atendeu = cursor.fetchone()[0]

        n_atendeu = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'NO ANSWER' AND src=%s AND tipo='%s'""" % (src_f, tipo_f)
        n_atendeu = cursor.execute(n_atendeu)
        n_atendeu = cursor.fetchone()[0]

        ocupado = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'BUSY' AND src=%s AND tipo='%s'""" % (src_f, tipo_f)
        ocupado = cursor.execute(ocupado)
        ocupado = cursor.fetchone()[0]

        falhou = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'FAILED' AND src=%s AND tipo='%s'""" % (src_f, tipo_f)
        falhou = cursor.execute(falhou)
        falhou = cursor.fetchone()[0]

        fixo = """SELECT Count(disposition) FROM vw_cdr WHERE tipo = 'FIXO' AND disposition = 'ANSWERED' AND src=%s AND tipo='%s'""" % (src_f, tipo_f)
        fixo = cursor.execute(fixo)
        fixo = cursor.fetchone()[0]

        movel = """SELECT Count(disposition) FROM vw_cdr WHERE tipo = 'MOVEL' AND disposition = 'ANSWERED' AND src=%s AND tipo='%s'""" % (src_f, tipo_f)
        movel = cursor.execute(movel)
        movel = cursor.fetchone()[0]

        radio = """SELECT Count(disposition) FROM vw_cdr WHERE tipo = 'RADIO' AND disposition = 'ANSWERED' AND src=%s AND tipo='%s'""" % (src_f, tipo_f)
        radio = cursor.execute(radio)
        radio = cursor.fetchone()[0]

    elif tipo_f == '':

        atendeu = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'ANSWERED' AND src=%s AND operadora ='%s'""" % (src_f, operadora_f)
        atendeu = cursor.execute(atendeu)
        atendeu = cursor.fetchone()[0]

        n_atendeu = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'NO ANSWER' AND src=%s AND operadora ='%s'""" % (src_f, operadora_f)
        n_atendeu = cursor.execute(n_atendeu)
        n_atendeu = cursor.fetchone()[0]

        ocupado = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'BUSY' AND src=%s AND operadora ='%s'""" % (src_f, operadora_f)
        ocupado = cursor.execute(ocupado)
        ocupado = cursor.fetchone()[0]

        falhou = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'FAILED' AND src=%s AND operadora ='%s'""" % (src_f, operadora_f)
        falhou = cursor.execute(falhou)
        falhou = cursor.fetchone()[0]

        fixo = """SELECT Count(disposition) FROM vw_cdr WHERE tipo = 'FIXO' AND disposition = 'ANSWERED' AND src=%s AND operadora ='%s'""" % (src_f, operadora_f)
        fixo = cursor.execute(fixo)
        fixo = cursor.fetchone()[0]

        movel = """SELECT Count(disposition) FROM vw_cdr WHERE tipo = 'MOVEL' AND disposition = 'ANSWERED' AND src=%s AND operadora ='%s'""" % (src_f, operadora_f)
        movel = cursor.execute(movel)
        movel = cursor.fetchone()[0]

        radio = """SELECT Count(disposition) FROM vw_cdr WHERE tipo = 'RADIO' AND disposition = 'ANSWERED' AND src=%s AND operadora ='%s'""" % (src_f, operadora_f)
        radio = cursor.execute(radio)
        radio = cursor.fetchone()[0]


    elif operadora_f == '' and tipo_f == '':

        atendeu = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'ANSWERED' AND src==%s""" % (src_f)
        atendeu = cursor.execute(atendeu)
        atendeu = cursor.fetchone()[0]

        n_atendeu = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'NO ANSWER' AND src==%s""" % (src_f)
        n_atendeu = cursor.execute(n_atendeu)
        n_atendeu = cursor.fetchone()[0]

        ocupado = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'BUSY' AND src==%s""" % (src_f)
        ocupado = cursor.execute(ocupado)
        ocupado = cursor.fetchone()[0]

        falhou = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'FAILED' AND src==%s""" % (src_f)
        falhou = cursor.execute(falhou)
        falhou = cursor.fetchone()[0]

        fixo = """SELECT Count(disposition) FROM vw_cdr WHERE tipo = 'FIXO' AND disposition = 'ANSWERED' AND src==%s""" % (src_f)
        fixo = cursor.execute(fixo)
        fixo = cursor.fetchone()[0]

        movel = """SELECT Count(disposition) FROM vw_cdr WHERE tipo = 'MOVEL' AND disposition = 'ANSWERED' AND src==%s""" % (src_f)
        movel = cursor.execute(movel)
        movel = cursor.fetchone()[0]

        radio = """SELECT Count(disposition) FROM vw_cdr WHERE tipo = 'RADIO' AND disposition = 'ANSWERED' AND src==%s""" % (src_f)
        radio = cursor.execute(radio)
        radio = cursor.fetchone()[0]

    else:

        atendeu = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'ANSWERED' AND src==%s AND operadora ='%s' AND tipo='%s'""" % (src_f, operadora_f, tipo_f)
        atendeu = cursor.execute(atendeu)
        atendeu = cursor.fetchone()[0]

        n_atendeu = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'NO ANSWER' AND src==%s AND operadora ='%s' AND tipo='%s'""" % (src_f, operadora_f, tipo_f)
        n_atendeu = cursor.execute(n_atendeu)
        n_atendeu = cursor.fetchone()[0]

        ocupado = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'BUSY' AND src==%s AND operadora ='%s' AND tipo='%s'""" % (src_f, operadora_f, tipo_f)
        ocupado = cursor.execute(ocupado)
        ocupado = cursor.fetchone()[0]

        falhou = """SELECT Count(disposition) FROM vw_cdr WHERE disposition = 'FAILED' AND src==%s AND operadora ='%s' AND tipo='%s'""" % (src_f, operadora_f, tipo_f)
        falhou = cursor.execute(falhou)
        falhou = cursor.fetchone()[0]

        fixo = """SELECT Count(disposition) FROM vw_cdr WHERE tipo = 'FIXO' AND disposition = 'ANSWERED' AND src==%s AND operadora ='%s' AND tipo='%s'""" % (src_f, operadora_f, tipo_f)
        fixo = cursor.execute(fixo)
        fixo = cursor.fetchone()[0]

        movel = """SELECT Count(disposition) FROM vw_cdr WHERE tipo = 'MOVEL' AND disposition = 'ANSWERED' AND src==%s AND operadora ='%s' AND tipo='%s'""" % (src_f, operadora_f, tipo_f)
        movel = cursor.execute(movel)
        movel = cursor.fetchone()[0]

        radio = """SELECT Count(disposition) FROM vw_cdr WHERE tipo = 'RADIO' AND disposition = 'ANSWERED' AND src==%s AND operadora ='%s' AND tipo='%s'""" % (src_f, operadora_f, tipo_f)
        radio = cursor.execute(radio)
        radio = cursor.fetchone()[0]

    ### FIM SQL personalizado

    if results:
        paginator = Paginator(results, int(paginas_f))
        page = request.GET.get('page')
      
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except (EmptyPage):
            results = paginator.page(paginator.num_pages)

        template = loader.get_template('cdr.html')
        context = RequestContext(request, {'byDay':byDay, 'byMonth':byMonth, 'ultimo':ultimo, 'results':results,
                                            'src':src, 'src_f':src_f ,'numero':numero, 'calldate':calldate, 'hoje':hoje, 'ontem':ontem, 
                                            'disposition':disposition, 'url':url, 'tempo_medio':tempo_medio, 'tempo':tempo, 'periodo_dia_1':periodo_dia_1,
                                            'periodo_dia_2':periodo_dia_2, 'periodo_mes_1':periodo_mes_1, 'periodo_mes_2':periodo_mes_2,
                                            'total':total, 'tempo_maior':tempo_maior, 'tempo_menor':tempo_menor, 'atendeu':atendeu,
                                            'n_atendeu':n_atendeu, 'ocupado':ocupado, 'falhou':falhou, 'fixo':fixo, 'movel':movel, 'radio':radio,
                                             'pagina': pagina, 'operadora': operadora,})
        return HttpResponse(template.render(context))
    else:
            template = loader.get_template('cdr.html')
            context = RequestContext(request, {'byDay':byDay, 'byMonth':byMonth, 'ultimo':ultimo, 'results':results,
                                            'src':src, 'src_f':src_f ,'numero':numero, 'calldate':calldate, 'hoje':hoje, 'ontem':ontem, 
                                            'disposition':disposition, 'url':url, 'tempo_medio':tempo_medio, 'tempo':tempo, 'periodo_dia_1':periodo_dia_1,
                                            'periodo_dia_2':periodo_dia_2, 'periodo_mes_1':periodo_mes_1, 'periodo_mes_2':periodo_mes_2,
                                            'total':total, 'tempo_maior':tempo_maior, 'tempo_menor':tempo_menor, 'atendeu':atendeu,
                                            'n_atendeu':n_atendeu, 'ocupado':ocupado, 'falhou':falhou, 'fixo':fixo, 'movel':movel, 'radio':radio,
                                            'pagina': pagina, 'operadora': operadora,})
            return HttpResponse(template.render(context))



