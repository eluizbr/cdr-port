from django.shortcuts import render
from django.http import HttpResponse
from models import Portados, NaoPortados,IpsPermitidos
from ratelimit.decorators import ratelimit


@ratelimit(key='ip', rate='30/m', block=True)
def consulta(request,numero):

	#rn1 = Portados.objects.values_list('rn1').filter(numero=numero)

	#rn1 = str(rn1)[5:7]
	rn1 = len(numero)

	try:

		ip_externo = request.META['REMOTE_ADDR']

		ipaddr = IpsPermitidos.objects.values_list('ipaddr').filter(ipaddr=ip_externo)[0]
		ipaddr = ipaddr[0]
	
		if ip_externo == ipaddr:


			if rn1 == 9:
				print numero
				rn1 = Portados.objects.values_list('rn1').filter(numero=numero)
				rn1 = str(rn1)[5:7]

				if not rn1:
					rn1 = str(numero)[0:6]
					rn1 = NaoPortados.objects.values_list('rn1').filter(prefixo=rn1)
					rn1 = str(rn1)[5:7]

			elif rn1 == 10:
				rn1 = Portados.objects.values_list('rn1').filter(numero=numero)
				rn1 = str(rn1)[5:7]

				if not rn1:
					rn1 = str(numero)[0:6]
					rn1 = NaoPortados.objects.values_list('rn1').filter(prefixo=rn1)
					rn1 = str(rn1)[5:7]

			elif rn1 == 11:
				rn1 = Portados.objects.values_list('rn1').filter(numero=numero)
				rn1 = str(rn1)[5:7]

				if not rn1:
					rn1 = str(numero)[0:7]
					rn1 = NaoPortados.objects.values_list('rn1').filter(prefixo=rn1)
					rn1 = str(rn1)[5:7]

			response = HttpResponse(rn1, content_type='text/plain')
			return response
		else:


			rn1 = 0
			response = HttpResponse(rn1, content_type='text/plain')
			return response
	except:

		rn1 = 0
		response = HttpResponse(rn1, content_type='text/plain')
		return response