from django.contrib import admin
from .models import Sip

class SipAdmin(admin.ModelAdmin):
	list_display = [ 'name', 'type', 'secret', 'context', 'host', 'ipaddr', 'regseconds', 'lastms']


admin.site.register(Sip, SipAdmin)


