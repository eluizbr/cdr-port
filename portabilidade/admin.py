from django.contrib import admin
from .models import IpsPermitidos

class IpsPermitidosAdmin(admin.ModelAdmin):
	list_display = ['nome', 'key']


admin.site.register(IpsPermitidos,IpsPermitidosAdmin)

