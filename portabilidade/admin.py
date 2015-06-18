from django.contrib import admin
from .models import AuthKey

class AuthKeyAdmin(admin.ModelAdmin):
	list_display = ['nome', 'key']


admin.site.register(AuthKey,AuthKeyAdmin)

