# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from django import forms
from models import Sip


class SipForm(forms.ModelForm):
	
	class Meta:
		model = Sip
		fields = ('name','secret','host', 'context', 'nat', 'type', 'allow', 'insecure')


		 