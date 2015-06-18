# -*- coding: UTF-8 -*-
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.utils.translation import ugettext_lazy as _

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

class Config_Local(models.Model):

    AUDIO =(
        ('Nao', 'Nao'),
        ('Sim', 'Sim'),
    )

    ddd = models.IntegerField(help_text=_("Insira seu DDD"),verbose_name="DDD")
    estado = models.ForeignKey(State ,help_text=_("Selecione a estado"),verbose_name="Estado")
    cidade = ChainedForeignKey(City, chained_field="estado", chained_model_field="id_state", auto_choose=True,verbose_name="Cidade",help_text=_("Selecione a cidade"))
    cortar = models.IntegerField(help_text=_("Numero de digitos a serem cortados. Ex: Se voce envia 551120304050, digite 2 para remover o 55."),verbose_name="Cortar")
    gravar = models.CharField(max_length=3,help_text=_("Selecione SIM, se voce grava ligacoes."),verbose_name="Audio",choices=AUDIO,default='Nao')
    custo_local = models.DecimalField(max_digits=10, decimal_places=2, blank=True, help_text=_("Custo Local"),default='0.00',verbose_name="Fixo")
    custo_ldn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, help_text=_("Custo LDN"),default='0.00',verbose_name="Fixo LDN")
    custo_movel_local = models.DecimalField(max_digits=10, decimal_places=2, blank=True, help_text=_("Movel Local"),default='0.00',verbose_name="Movel Local")
    custo_movel_ldn = models.DecimalField(max_digits=10, decimal_places=2, blank=True, help_text=_("Movel LDN"),default='0.00',verbose_name="Movel LDN")

    def __unicode__(self):
        return unicode(self.estado)

    class Meta:
        verbose_name='Configurações geral'


class Info(models.Model):
    uuid = models.CharField(max_length=100, blank=True)
    system_number = models.CharField(max_length=100, blank=True)
    system_name = models.CharField(max_length=100, blank=True)
    mac = models.CharField(max_length=20, blank=True)
    frequencia = models.CharField(max_length=20, blank=True)
    data_ativacao = models.DateTimeField(blank=True, null=True)
    data_expira = models.DateTimeField(blank=True, null=True)
    ativo = models.IntegerField(null=True, default='1')

    def __unicode__(self):
        return unicode(self.uuid)

class cdr(models.Model):
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    dcontext = models.CharField(max_length=80)
    channel = models.CharField(max_length=80)
    dstchannel = models.CharField(max_length=80)
    lastapp = models.CharField(max_length=80)
    lastdata = models.CharField(max_length=80)
    duration = models.IntegerField()
    billsec = models.IntegerField()
    disposition = models.CharField(max_length=45)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    uniqueid = models.CharField(unique=True, max_length=32)
    userfield = models.CharField(max_length=255, blank=True, null=True)
    prefix = models.CharField(max_length=80, blank=True, null=True)
    portado = models.CharField(max_length=3, default='Nao')
    
    def __unicode__(self):
        return unicode(self.dst)

class Cdrport(models.Model):
    calldate = models.DateTimeField(blank=True, null=True)
    src = models.BigIntegerField(blank=True, null=True)
    dst = models.BigIntegerField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    billsec = models.TimeField(blank=True, null=True)
    disposition = models.CharField(max_length=20)
    ddd = models.IntegerField(blank=True, null=True)
    prefixo = models.IntegerField(blank=True, null=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    operadora_id = models.CharField(max_length=50)
    tipo = models.CharField(max_length=6)
    rn1_id = models.IntegerField(blank=True, null=True)
    portado = models.CharField(max_length=5, blank=True)
    uniqueid = models.CharField(unique=True, max_length=32, blank=True)
    userfield = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.numero)

class Prefixo(models.Model):
    ddd = models.IntegerField(blank=True, null=True)
    prefixo = models.IntegerField(unique=True, blank=True, null=True)
    inicial = models.IntegerField(blank=True, null=True)
    final = models.IntegerField(blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    operadora = models.CharField(max_length=30, blank=True)
    tipo = models.CharField(max_length=20, blank=True)
    rn1 = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.ddd)
'''
class GeoLocal(models.Model):
    gm_ponto = models.TextField(blank=True)
    id = models.IntegerField(primary_key=True)
    cd_geocodigo = models.CharField(max_length=20)
    tipo = models.CharField(max_length=10, blank=True)
    cd_geocodba = models.CharField(max_length=20)
    nm_bairro = models.CharField(max_length=60, blank=True)
    cd_geocodsd = models.CharField(max_length=20)
    nm_subdistrito = models.CharField(max_length=60)
    cd_geocodds = models.CharField(max_length=20)
    nm_distrito = models.CharField(max_length=60)
    cd_geocodmu = models.CharField(max_length=20)
    nm_municipio = models.CharField(max_length=60)
    nm_micro = models.CharField(max_length=100, blank=True)
    nm_meso = models.CharField(max_length=100, blank=True)
    nm_uf = models.CharField(max_length=60, blank=True)
    cd_nivel = models.CharField(max_length=1)
    cd_categoria = models.CharField(max_length=5)
    nm_categoria = models.CharField(max_length=50)
    nm_localidade = models.CharField(max_length=60)
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    alt = models.FloatField(blank=True, null=True)
    gm_ponto_sk = models.CharField(max_length=15, blank=True)

    def __unicode__(self):
        return unicode(self.nm_municipio)
'''
class DispositionPercent(models.Model):
    disposition = models.CharField(unique=True, max_length=30)
    valor = models.IntegerField(blank=True, null=True)
    perc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.disposition)

class VwDayStats(models.Model):
    dia = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    total = models.BigIntegerField()
    
    def __unicode__(self):
        return unicode(self.dia)
    class Meta:
        managed = False
        db_table = 'vw_day_stats'

class VwMonthStats(models.Model):
    mes = models.CharField(max_length=9, blank=True)
    total = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'vw_month_stats'

class VwLast10(models.Model):
    dst = models.CharField(max_length=80)
    operadora = models.CharField(max_length=30, blank=True)
    tipo = models.CharField(max_length=5, blank=True)
    rn1 = models.IntegerField(blank=True, null=True)
    calldate = models.DateTimeField()
    disposition = models.CharField(max_length=45)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    portado = models.CharField(max_length=3, blank=True)

    class Meta:
        managed = False
        db_table = 'vw_last_10'


class VwOperadoras(models.Model):
    operadora = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    total = models.BigIntegerField()

    def __unicode__(self):
        return unicode(self.operadora)
        
    class Meta:
        managed = False
        db_table = 'vw_operadoras'

class VwStatsAnswered(models.Model):
    dia = models.BigIntegerField(blank=True, null=True)
    semana = models.BigIntegerField(blank=True, null=True)
    mes = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_stats_answered'


class VwStatsBusy(models.Model):
    dia = models.BigIntegerField(blank=True, null=True)
    semana = models.BigIntegerField(blank=True, null=True)
    mes = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_stats_busy'


class VwStatsNoanswer(models.Model):
    dia = models.BigIntegerField(blank=True, null=True)
    semana = models.BigIntegerField(blank=True, null=True)
    mes = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_stats_noanswer'

class VwRamais(models.Model):
    ramais = models.CharField(max_length=80)
#    total = models.BigIntegerField()

    def __unicode__(self):
        return unicode(self.ramais)
        
    class Meta:
        managed = False
        db_table = 'vw_ramais'

class VwDisposition(models.Model):
    disposition = models.CharField(max_length=45)
    total = models.BigIntegerField()

    def __unicode__(self):
        return unicode(self.disposition)

    class Meta:
        managed = False
        db_table = 'vw_disposition'

class VwCidades(models.Model):
    cidade = models.CharField(max_length=100, blank=True)
#    total = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'vw_cidades'

    def __unicode__(self):
        return unicode(self.cidade)

class VwEstados(models.Model):
    estado = models.CharField(max_length=2, blank=True)
    total = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'vw_estados'
    
    def __unicode__(self):
        return unicode(self.estado)

class VwCdr(models.Model):
    calldate = models.DateTimeField()
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    duration = models.TimeField(blank=True, null=True)
    billsec = models.TimeField(blank=True, null=True)
    disposition = models.CharField(max_length=45)
    ddd = models.IntegerField(blank=True, null=True)
    prefixo = models.IntegerField(blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    operadora = models.CharField(max_length=30, blank=True)
    tipo = models.CharField(max_length=5, blank=True)
    rn1 = models.IntegerField(blank=True, null=True)
    portado = models.CharField(max_length=3, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
    userfield = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return unicode(self.dst)
    class Meta:
        managed = False
        db_table = 'vw_cdr'
