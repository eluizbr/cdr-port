from django.contrib import admin
from .models import Cadastro,ServerCliente



class ServerClienteAdmin(admin.ModelAdmin):
	list_display = [ 'id_cliente', 'nome_servidor','ip_servidor','plano', 'status','setup','criacao','ativacao']

admin.site.register(Cadastro)
admin.site.register(ServerCliente,ServerClienteAdmin)


