from django.contrib import admin
from .models import IpsPermitidos

class IpsPermitidosAdmin(admin.ModelAdmin):
	list_display = ['IP']


admin.site.register(IpsPermitidos)

