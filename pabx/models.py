# coding:utf-8
from django.db import models
from choices import TYPE, TRANSPORT, DTMFMODE, DIRECTMEDIA, NAT, TRUSTRPID, PROGRESSINBAND, PROMISCREDIR, USECLIENTCODE, CALLCOUNTER,\
                    ALLOWOVERLAP, ALLOWSUBSCRIBE, VIDEOSEUPPORT, RFC2833COMPENSATE, SEESIONTIMERS, SEESIONREFRESHER, SENDRPID, REGISTERTRYING,\
                    CONSTANTSSRC, USEREQPHONE, TEXTSUPPORT, FAXDETECT, BUGGYMWI, CALLINGPRES, HASVOICEMAIL, SUBSCRIBEMWI, AUTOFRAMING, G726NONSTANDARD,\
                    IGNORESDPVERSION, ALLOWTRANSFER, DYNAMIC 


'''
class rt_calls(models.Model):
    Event = models.CharField(blank=True, null=True, max_length=100)
    Channel = models.CharField(blank=True, null=True, max_length=100)
    ChannelState = models.IntegerField()
    ChannelStateDesc = models.CharField(blank=True, null=True, max_length=10)
    CallerIDNum = models.IntegerField(blank=True, null=True, max_length=40)
    CallerIDName = models.CharField(max_length=100)
    ConnectedLineNum = models.CharField(blank=True, null=True, max_length=100)
    ConnectedLineName = models.CharField(blank=True, null=True, max_length=100)
    Language = models.CharField(blank=True, null=True, max_length=10)
    AccountCode = models.CharField(blank=True, null=True, max_length=100)
    Context = models.CharField(blank=True, null=True, max_length=100)
    Exten = models.CharField(blank=True, null=True, max_length=100)
    Priority = models.IntegerField(blank=True, null=True, max_length=10)
    Uniqueid = models.CharField(unique=True, max_length=100)
    Application = models.CharField(blank=True, null=True, max_length=100)
    ApplicationData = models.CharField(blank=True, null=True, max_length=100)
    Duration = models.TimeField()
    BridgeId = models.CharField(unique=True, blank=True, null=True, max_length=200)
    controle = models.IntegerField(max_length=1, default=0, blank=True, null=True)
    
    def __unicode__(self):
        return "%s %s %s" %(self.ChannelState, self.ChannelStateDesc, self.controle)

'''

class rt_calls(models.Model):
    Channel = models.CharField(blank=True, null=True, max_length=100)
    ChannelState = models.IntegerField()
    ChannelStateDesc = models.CharField(blank=True, null=True, max_length=10)
    CallerIDNum = models.IntegerField(blank=True, null=True, max_length=40)
    CallerIDName = models.CharField(max_length=100)
    ConnectedLineNum = models.CharField(blank=True, null=True, max_length=100)
    ConnectedLineName = models.CharField(blank=True, null=True, max_length=100)
    AccountCode = models.CharField(blank=True, null=True, max_length=100)
    Context = models.CharField(blank=True, null=True, max_length=100)
    Exten = models.CharField(blank=True, null=True, max_length=100)
    Priority = models.IntegerField(blank=True, null=True, max_length=10)
    Uniqueid = models.CharField(max_length=100)
    Application = models.CharField(blank=True, null=True, max_length=100)
    Duration = models.TimeField()
    BridgeId = models.CharField(blank=True, null=True, max_length=200)
    controle = models.IntegerField(max_length=1, default=0, blank=True, null=True)
    ipaddr = models.CharField(max_length=15,blank=True, null=True)
    lastms = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
       # return "%s %s %s" %(self.ChannelState, self.ChannelStateDesc, self.controle)
       return unicode(self.ChannelState)




class Sip(models.Model):
    name = models.CharField(u'Ramal', unique=True, max_length=10)
    ipaddr = models.CharField(u'IP', max_length=15, blank=True, default='0.0.0.0')
    port = models.IntegerField(blank=True, null=True, default='5060')
    regseconds = models.IntegerField(blank=True, null=True)
    defaultuser = models.CharField(max_length=10, blank=True)
    fullcontact = models.CharField(max_length=250, blank=True)
    regserver = models.CharField(max_length=20, blank=True)
    useragent = models.CharField(max_length=50, blank=True)
    lastms = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=40, blank=True, default='dynamic')
    type = models.CharField(max_length=6, blank=True, choices=TYPE, default='friend')
    context = models.CharField(max_length=40, blank=True, default='default')
    permit = models.CharField(max_length=40, blank=True)
    deny = models.CharField(max_length=40, blank=True)
    secret = models.CharField(u'Senha', max_length=40, blank=True)
    md5secret = models.CharField(max_length=40, blank=True)
    remotesecret = models.CharField(max_length=40, blank=True)
    transport = models.CharField(max_length=7, blank=True, choices=TRANSPORT, default='udp')
    dtmfmode = models.CharField(max_length=9, blank=True, choices=DTMFMODE, default='rfc2833')
    directmedia = models.CharField(max_length=6, blank=True, choices=DIRECTMEDIA, default='no')
    nat = models.CharField(max_length=25, blank=True, choices=NAT, default='no')
    callgroup = models.CharField(max_length=40, blank=True)
    pickupgroup = models.CharField(max_length=40, blank=True)
    language = models.CharField(max_length=40, blank=True)
    allow = models.CharField(max_length=40, blank=True, default='ulaw,alaw,gsm,g729')
    disallow = models.CharField(max_length=40, blank=True)
    insecure = models.CharField(max_length=40, blank=True, default='port,invite')
    trustrpid = models.CharField(max_length=3, blank=True, choices=TRUSTRPID, default='no')
    progressinband = models.CharField(max_length=5, blank=True, choices=PROGRESSINBAND, default='no')
    promiscredir = models.CharField(max_length=3, blank=True, choices=PROMISCREDIR, default='no')
    useclientcode = models.CharField(max_length=3, blank=True, choices=USECLIENTCODE, default='no')
    accountcode = models.CharField(max_length=40, blank=True)
    setvar = models.CharField(max_length=40, blank=True)
    callerid = models.CharField(max_length=40, blank=True)
    amaflags = models.CharField(max_length=40, blank=True)
    callcounter = models.CharField(max_length=3, blank=True, choices=CALLCOUNTER, default='no')
    busylevel = models.IntegerField(blank=True, null=True)
    allowoverlap = models.CharField(max_length=3, blank=True, choices=ALLOWOVERLAP, default='no')
    allowsubscribe = models.CharField(max_length=3, blank=True, choices=ALLOWSUBSCRIBE, default='no')
    videosupport = models.CharField(max_length=3, blank=True, choices=VIDEOSEUPPORT, default='no')
    maxcallbitrate = models.IntegerField(blank=True, null=True)
    rfc2833compensate = models.CharField(max_length=3, blank=True, choices=RFC2833COMPENSATE, default='no')
    mailbox = models.CharField(max_length=40, blank=True)
    session_timers = models.CharField(db_column='session-timers', max_length=9, blank=True, choices=SEESIONTIMERS, default='refuse')
    session_expires = models.IntegerField(db_column='session-expires', blank=True, null=True)
    session_minse = models.IntegerField(db_column='session-minse', blank=True, null=True)
    session_refresher = models.CharField(db_column='session-refresher', max_length=3, blank=True, choices=SEESIONREFRESHER, default='uac')
    t38pt_usertpsource = models.CharField(max_length=40, blank=True)
    regexten = models.CharField(max_length=40, blank=True)
    fromdomain = models.CharField(max_length=40, blank=True)
    fromuser = models.CharField(max_length=40, blank=True)
    qualify = models.CharField(max_length=40, blank=True, default='yes')
    defaultip = models.CharField(max_length=40, blank=True)
    rtptimeout = models.IntegerField(blank=True, null=True)
    rtpholdtimeout = models.IntegerField(blank=True, null=True)
    sendrpid = models.CharField(max_length=3, blank=True, choices=SENDRPID, default='no')
    outboundproxy = models.CharField(max_length=40, blank=True)
    callbackextension = models.CharField(max_length=40, blank=True)
    registertrying = models.CharField(max_length=3, blank=True, choices=REGISTERTRYING, default='no')
    timert1 = models.IntegerField(blank=True, null=True)
    timerb = models.IntegerField(blank=True, null=True)
    qualifyfreq = models.IntegerField(blank=True, null=True)
    constantssrc = models.CharField(max_length=3, blank=True, choices=CONSTANTSSRC, default='no')
    contactpermit = models.CharField(max_length=40, blank=True)
    contactdeny = models.CharField(max_length=40, blank=True)
    usereqphone = models.CharField(max_length=3, blank=True, choices=USEREQPHONE, default='no')
    textsupport = models.CharField(max_length=3, blank=True, choices=TEXTSUPPORT, default='no')
    faxdetect = models.CharField(max_length=3, blank=True, choices=FAXDETECT, default='no')
    buggymwi = models.CharField(max_length=3, blank=True, choices=BUGGYMWI, default='no')
    auth = models.CharField(max_length=40, blank=True)
    fullname = models.CharField(max_length=40, blank=True)
    trunkname = models.CharField(max_length=40, blank=True)
    cid_number = models.CharField(max_length=40, blank=True)
    callingpres = models.CharField(max_length=21, blank=True, choices=CALLINGPRES, default='allowed')
    mohinterpret = models.CharField(max_length=40, blank=True)
    mohsuggest = models.CharField(max_length=40, blank=True)
    parkinglot = models.CharField(max_length=40, blank=True)
    hasvoicemail = models.CharField(max_length=3, blank=True, choices=HASVOICEMAIL, default='no')
    subscribemwi = models.CharField(max_length=3, blank=True, choices=SUBSCRIBEMWI, default='no')
    vmexten = models.CharField(max_length=40, blank=True)
    autoframing = models.CharField(max_length=3, blank=True, choices=AUTOFRAMING, default='no')
    rtpkeepalive = models.IntegerField(blank=True, null=True)
    call_limit = models.IntegerField(db_column='call-limit', blank=True, null=True)
    g726nonstandard = models.CharField(max_length=3, blank=True, choices=G726NONSTANDARD, default='no')
    ignoresdpversion = models.CharField(max_length=3, blank=True, choices=IGNORESDPVERSION, default='no')
    allowtransfer = models.CharField(max_length=3, blank=True, choices=ALLOWTRANSFER, default='yes')
    dynamic = models.CharField(max_length=3, blank=True, choices=DYNAMIC, default='yes')

    def __unicode__(self):
        return unicode(self.name)


'''
    class Meta:
        managed = False
        db_table = 'sip'
'''

class VwSipregs(models.Model):
    name = models.CharField(max_length=80)
    ipaddr = models.CharField(max_length=15)
    port = models.IntegerField()
    regseconds = models.IntegerField()
    defaultuser = models.CharField(max_length=80)
    fullcontact = models.CharField(max_length=80)
    regserver = models.CharField(max_length=100, blank=True)
    useragent = models.CharField(max_length=20, blank=True)
    lastms = models.IntegerField()
    callerid = models.CharField(max_length=40, blank=True)


    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        managed = False
        db_table = 'vw_sipregs'


class VwCall(models.Model):
    origem = models.CharField(max_length=50, blank=True)
    destino = models.CharField(max_length=100, blank=True)
    ramal = models.CharField(max_length=10)
    ip = models.CharField(max_length=15)
    lastms = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True)
    tempo = models.TimeField()
    controle = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_call'


'''
class Cel(models.Model):
    eventtype = models.CharField(max_length=30)
    eventtime = models.DateTimeField()
    userdeftype = models.CharField(max_length=255)
    cid_name = models.CharField(max_length=80)
    cid_num = models.CharField(max_length=80)
    cid_ani = models.CharField(max_length=80)
    cid_rdnis = models.CharField(max_length=80)
    cid_dnid = models.CharField(max_length=80)
    exten = models.CharField(max_length=80)
    context = models.CharField(max_length=80)
    channame = models.CharField(max_length=80)
    appname = models.CharField(max_length=80)
    appdata = models.CharField(max_length=80)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    peeraccount = models.CharField(max_length=20)
    uniqueid = models.CharField(max_length=150)
    linkedid = models.CharField(max_length=150)
    userfield = models.CharField(max_length=255)
    peer = models.CharField(max_length=80)
    extra = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.eventtype)

    class Meta:
        managed = False
        db_table = 'cel'
'''