from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import cdr, DispositionPercent, Stats_ANSWERED, Stats_NOANSWER, Stats_BUSY
from django.db.models import Sum, Count, Avg, Max, Min

def index(request):
    perc = DispositionPercent.objects.values_list('disposition', 'valor', 'perc')
    total = DispositionPercent.objects.aggregate(Sum('valor'))['valor__sum']
    stats_AN = Stats_ANSWERED.objects.values_list('d_total', 's_total', 'm_total')
    stats_NO = Stats_NOANSWER.objects.values_list('d_total', 's_total', 'm_total')
    stats_BU = Stats_BUSY.objects.values_list('d_total', 's_total', 'm_total')
    ultimo = cdr.objects.values_list('dst','calldate').order_by('-calldate')
    template = loader.get_template('index.html')
    context = RequestContext(request, {'perc': perc, 'total': total, 'stats_AN':stats_AN, 'stats_NO':stats_NO, 'stats_BU':stats_BU, 'ultimo':ultimo })
    return HttpResponse(template.render(context))


