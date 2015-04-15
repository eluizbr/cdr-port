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

    class Meta:
        managed = False
        db_table = 'vw_day_stats'