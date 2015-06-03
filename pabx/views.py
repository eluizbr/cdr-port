# coding:utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.template import RequestContext, loader, Template
from forms import SipForm
from pabx.models import VwSipregs, rt_calls, VwCall, Sip
from cdr.models import Info
from datetime import datetime, timedelta, time
import asterisk_stats as asterisk
import simplejson as json
from django.db.models import F, Q
import funcoes as funcao


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

	# Gerar ligação entre ramais

	origem_f = request.GET.get('origem', "")
	destino_f = request.GET.get('destino', "")

	if request.GET.get('origem_f','destino_f'):
		funcao.gerar_call(origem_f,destino_f)

	# FIM Gerar ligação entre ramais

	exten = rt_calls.objects.all()
	
	info = Info.objects.values_list('ativo')
	info = str(info)[2]
	troncos = asterisk.stats_request('SIPshowregistry')
	ramais_sip = VwSipregs.objects.all()

	template = loader.get_template('mesa.html')
	context = RequestContext(request, {'info':info,'exten':exten, 'ramais_sip':ramais_sip, 'troncos':troncos})
	return HttpResponse(template.render(context))

	
def editar_ramal(request,name):



	
	
	sip = get_object_or_404(Sip, name=name)
	secret_f = request.GET.get('secret', "")
	codec_f = request.GET.get('allow', "")
	#print request.method 
	
	if request.method == 'POST':

		sip = get_object_or_404(Sip, name=name)
		secret_f = request.GET.get('secret', "")
		codec_f = request.GET.get('allow', "")

	else:
		ramal = Sip.objects.get(name=name)
		ramal.secret = secret_f
		ramal.allow = codec_f
		#ramal.secret = make_password(password=secret_f,hasher='md5')
		#print secret_f
		ramal.save()
	

	return render(request, 'editar_ramal.html', {'secret_f':secret_f,'codec_f':codec_f,'sip':sip})


	'''

	sip = get_object_or_404(Sip, name=name)
	#secret_f = request.GET.get('secret', "")
	#print secret_f
	#print request

	if request.method == 'POST':
		form = SipForm(request.POST, instance=sip)
		
		if form.is_valid():
			form.save()
			messages.success(request, 'Ramal alterado')
			#return HttpResponseRedirect('/ramal-alterado/')
	else:
		form = SipForm(instance=sip)

	return render(request, 'editar_ramal.html', {'sip':sip, 'form':form})

	'''
	

def editar_ramal_ok(request):

	sip = Sip.objects.all()

	
	return render_to_response("ok_ramal.html", {'sip':sip})

