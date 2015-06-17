from django.db import models


class NaoPortados(models.Model):
    operadora = models.CharField(max_length=64)
    tipo = models.CharField(max_length=64)
    prefixo = models.BigIntegerField()
    rn1 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nao_portados'


class Portados(models.Model):
    numero = models.BigIntegerField()
    rn1 = models.IntegerField()
    data_hora = models.DateTimeField()
    op = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'portados'


class IpsPermitidos(models.Model):

    ipaddr = models.GenericIPAddressField()

    def __unicode__(self):
        return unicode(self.ipaddr)