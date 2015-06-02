# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from django import forms
from models import Sip
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class SipForm(forms.ModelForm):
	
	class Meta:
		model = Sip
		fields = ('secret','host', 'context', 'nat', 'type', 'allow')


	        
        helper = FormHelper()
        helper.form_class = 'form-horizontal'
        helper.layout = Layout(
         	
        	Field('secret', type="password", title="Digite a senha", css_class="passwordfields"),


       		)

        helper.add_input(Submit('submit', 'Salvar'))
