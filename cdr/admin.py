# -*- coding: UTF-8 -*-
from django.contrib import admin
from .models import Config_Local

class Config_LocalAdmin(admin.ModelAdmin):
	list_display = ['ddd', 'estado', 'cidade', 'cortar', 'gravar', 'custo_local', 'custo_ldn', 'custo_movel_local', 'custo_movel_ldn']


admin.site.register(Config_Local, Config_LocalAdmin)

