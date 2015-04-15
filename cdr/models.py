from django.db import models


class cdr(models.Model):
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80, db_index=True)
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
    uniqueid = models.CharField(max_length=32)
    userfield = models.CharField(max_length=255)
    
    def __unicode__(self):
        return unicode(self.dst)

class GeoLocal(models.Model):
    gm_ponto = models.TextField(db_column='GM_PONTO', blank=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cd_geocodigo = models.CharField(db_column='CD_GEOCODIGO', max_length=20)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=10, blank=True)  # Field name made lowercase.
    cd_geocodba = models.CharField(db_column='CD_GEOCODBA', max_length=20)  # Field name made lowercase.
    nm_bairro = models.CharField(db_column='NM_BAIRRO', max_length=60, blank=True)  # Field name made lowercase.
    cd_geocodsd = models.CharField(db_column='CD_GEOCODSD', max_length=20)  # Field name made lowercase.
    nm_subdistrito = models.CharField(db_column='NM_SUBDISTRITO', max_length=60)  # Field name made lowercase.
    cd_geocodds = models.CharField(db_column='CD_GEOCODDS', max_length=20)  # Field name made lowercase.
    nm_distrito = models.CharField(db_column='NM_DISTRITO', max_length=60)  # Field name made lowercase.
    cd_geocodmu = models.CharField(db_column='CD_GEOCODMU', max_length=20)  # Field name made lowercase.
    nm_municipio = models.CharField(db_column='NM_MUNICIPIO', max_length=60)  # Field name made lowercase.
    nm_micro = models.CharField(db_column='NM_MICRO', max_length=100, blank=True)  # Field name made lowercase.
    nm_meso = models.CharField(db_column='NM_MESO', max_length=100, blank=True)  # Field name made lowercase.
    nm_uf = models.CharField(db_column='NM_UF', max_length=60, blank=True)  # Field name made lowercase.
    cd_nivel = models.CharField(db_column='CD_NIVEL', max_length=1)  # Field name made lowercase.
    cd_categoria = models.CharField(db_column='CD_CATEGORIA', max_length=5)  # Field name made lowercase.
    nm_categoria = models.CharField(db_column='NM_CATEGORIA', max_length=50)  # Field name made lowercase.
    nm_localidade = models.CharField(db_column='NM_LOCALIDADE', max_length=60)  # Field name made lowercase.
    long = models.FloatField(db_column='LONG', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='LAT', blank=True, null=True)  # Field name made lowercase.
    alt = models.FloatField(db_column='ALT', blank=True, null=True)  # Field name made lowercase.
    gm_ponto_sk = models.CharField(db_column='GM_PONTO_sk', max_length=15, blank=True)  # Field name made lowercase.

    def __unicode__(self):
        return unicode(self.nm_municipio)

class DispositionPercent(models.Model):
    disposition = models.CharField(unique=True, max_length=30)
    valor = models.IntegerField(blank=True, null=True)
    perc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.disposition)

class Stats_ANSWERED(models.Model):
    d_total = models.IntegerField(unique=True, blank=True, null=True)
    s_total = models.IntegerField(blank=True, null=True)
    m_total = models.IntegerField(blank=True, null=True)

class Stats_NOANSWER(models.Model):
    d_total = models.IntegerField(unique=True, blank=True, null=True)
    s_total = models.IntegerField(blank=True, null=True)
    m_total = models.IntegerField(blank=True, null=True)

class Stats_BUSY(models.Model):
    d_total = models.IntegerField(unique=True, blank=True, null=True)
    s_total = models.IntegerField(blank=True, null=True)
    m_total = models.IntegerField(blank=True, null=True)

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
    calldate = models.DateTimeField()
    billsec = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vw_last_10'

class VwOperadoras(models.Model):
    operadora = models.CharField(max_length=64)
    total = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'vw_operadoras'