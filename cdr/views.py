from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from .models import cdr, DispositionPercent, Stats_ANSWERED, Stats_NOANSWER, Stats_BUSY
from .models import VwDayStats, VwMonthStats,VwLast10, VwOperadoras
from django.db.models import Sum, Count, Avg, Max, Min

def index(request):
    perc = DispositionPercent.objects.values_list('disposition', 'valor', 'perc')
    total = DispositionPercent.objects.aggregate(Sum('valor'))['valor__sum']
    stats_AN = Stats_ANSWERED.objects.values_list('d_total', 's_total', 'm_total')
    stats_NO = Stats_NOANSWER.objects.values_list('d_total', 's_total', 'm_total')
    stats_BU = Stats_BUSY.objects.values_list('d_total', 's_total', 'm_total')
    ultimo = VwLast10.objects.values_list('numero','calldate','billsec')
    byDay = VwDayStats.objects.values_list('dia', 'mes', 'total')
    byMonth = VwMonthStats.objects.values_list('mes', 'total')
    operadora = VwOperadoras.objects.values_list('operadora', 'total')
    template = loader.get_template('index.html')
    context = RequestContext(request, {'perc': perc, 'total': total, 'stats_AN':stats_AN, 'stats_NO':stats_NO,
								    	'stats_BU':stats_BU, 'ultimo':ultimo, 'byDay':byDay, 'byMonth':byMonth, 'operadora':operadora })
    return HttpResponse(template.render(context))


def time_line(request):
    ultimo = VwLast10.objects.values_list('numero','operadora','tipo','calldate', 'disposition' ,'billsec')
    resultado = cdr.objects.values_list('dst', 'src', 'calldate', 'disposition', 'duration', 'billsec').order_by('-calldate')
    paginator = Paginator(resultado, 15)

    page = request.GET.get('page', '1')

    try:
        results = paginator.page(page)
    except(EmptyPage, InvalidPage):
        results = paginator.page(paginator.num_pages)


    template = loader.get_template('cdr.html')
    context = RequestContext(request, {'ultimo':ultimo, 'results':results })
    return HttpResponse(template.render(context))