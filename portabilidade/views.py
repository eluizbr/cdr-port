from django.shortcuts import render
from django.http import HttpResponse
from models import Portados, NaoPortados,AuthKey
from ratelimit.decorators import ratelimit


@ratelimit(key='ip', rate='60/m', block=True)
def consulta(request,numero):

	rn1 = len(numero)

	try:

		key = request.GET['key']
		key = str(key)

		chave = AuthKey.objects.values_list('key').filter(key=key)[0]
		chave = chave[0]
		chave = str(chave)

		if key == chave:

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