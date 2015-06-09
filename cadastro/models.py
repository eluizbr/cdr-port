# -*- coding: UTF-8 -*-
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.contrib.auth.models import User


class UserProfile(models.Model):

	user = models.OneToOneField(User, related_name='user_profile')


class State(models.Model):

    id_region = models.IntegerField()
    title = models.CharField(max_length=35)
    letter = models.CharField(max_length=2)
    iso = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        managed = False
        db_table = 'state'

class City(models.Model):
    id_state = models.ForeignKey('State', db_column='id_state')
    cidade = models.CharField(max_length=50)
    iso = models.IntegerField()
    iso_ddd = models.CharField(max_length=6)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1)
    
    def __unicode__(self):
        return unicode(self.cidade)

    class Meta:
        managed = False
        db_table = 'city'

class Cidades(models.Model):
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    ddd = models.IntegerField(blank=True, null=True)
    regiao = models.CharField(max_length=25, blank=True)

    def __unicode__(self):
        return unicode(self.estado)

    class Meta:
        managed = False
        db_table = 'cidades'

class Cadastro(models.Model):


    TIPO =(
	    ('fisca', 'Pessoa Fisca'),
	    ('jurica', 'Pessoa Jurica'),
    )


    tipo = models.CharField(u'Tipo',max_length=10,choices=TIPO)
    cpf = models.CharField(u'CPF',max_length=20,blank=True, null=True)
    cnpj = models.CharField(u'CNPJ',max_length=20,blank=True, null=True)
    telefone = models.CharField(u'Telefone',max_length=20,blank=True, null=True)
    email = models.EmailField('Email',max_length=254,blank=True, null=True)
    nome = models.CharField(u'Nome',max_length=100,blank=True, null=True)
    endereco = models.CharField(u'Endereço',max_length=100)
    numero = models.CharField(u'Número',max_length=100)
    bairro = models.CharField(u'Bairro',max_length=100,blank=True, null=True)
    complemento = models.CharField(u'Complento',max_length=100)
    estado = models.ForeignKey(State ,help_text=_("Selecione a estado"),verbose_name="Estado",blank=True, null=True)
    cidade = ChainedForeignKey(City, chained_field="estado", chained_model_field="id_state", auto_choose=True,verbose_name="Cidade",help_text=_("Selecione a cidade"))
    cod_cliente = models.IntegerField(u'Codigo do Cliente',max_length=100)

    def __unicode__(self):
       return "%s - %s" %(self.cod_cliente, self.nome)


class ServerCliente(models.Model):


    ATIVO =(
	    ('Sim', 'Sim'),
	    ('Nao', 'Nao'),
    )

    PLANO =(
	    ('Free', 'Free'),
	    ('Premium', 'Premium'),
    )

    id_cliente = models.ForeignKey('Cadastro', db_column='cod_cliente')
    nome_servidor = models.CharField(u'Nome do servidor',max_length=100)
    ip_servidor = models.CharField(u'IP do servidor',max_length=100)
    plano = models.CharField(u'Plano do servidor',max_length=100,choices=PLANO,default='Free')
    status = models.CharField(u'Ativo',max_length=10,choices=ATIVO)
    setup = models.IntegerField(max_length=1, default='0')
    criacao = models.DateTimeField(auto_now_add=True,blank=True,default=datetime.now)
    ativacao = models.DateTimeField(null=True,blank=True,auto_now=False, auto_now_add=False)


    def __unicode__(self):
        return unicode(self.id_cliente)