# coding:utf-8
TYPE= (
    ('friend', 'friend'),
    ('user', 'user'),
    ('peer', 'peer'),
)

TRANSPORT= (
    ('udp', 'udp'),
    ('tcp', 'tcp'),
    ('udp,tcp','udp,tcp'),
    ('tcp,udp','tcp,udp'),
)

DTMFMODE= (
    ('rfc2833', 'rfc2833'),
    ('info', 'info'),
    ('shortinfo', 'shortinfo'),
    ('inband', 'inband'),
    ('auto', 'auto'),
)

DIRECTMEDIA= (
    ('yes', 'yes'),
    ('no', 'no'),
    ('nonat', 'nonat'),
    ('update', 'update'),
)

NAT= (
    ('yes', 'yes'),
    ('no', 'no'),
    ('never', 'never'),
    ('route', 'route'),
    ('force_rport,comedia', 'force_port,comedia'),
)

TRUSTRPID= (
    ('yes', 'yes'),
    ('no', 'no'),
)

PROGRESSINBAND= (
    ('yes', 'yes'),
    ('no', 'no'),
    ('never', 'never'),
)

PROMISCREDIR= (
    ('yes', 'yes'),
    ('no', 'no'),
)

USECLIENTCODE= (
    ('yes', 'yes'),
    ('no', 'no'),
)

CALLCOUNTER= (
    ('yes', 'yes'),
    ('no', 'no'),
)

ALLOWOVERLAP= (
    ('yes', 'yes'),
    ('no', 'no'),
)

ALLOWSUBSCRIBE= (
    ('yes', 'yes'),
    ('no', 'no'),
)

VIDEOSEUPPORT= (
    ('yes', 'yes'),
    ('no', 'no'),
)

RFC2833COMPENSATE= (
    ('yes', 'yes'),
    ('no', 'no'),
)

SEESIONTIMERS= (
    ('accept', 'accept'),
    ('refuse', 'refuse'),
    ('originate', 'originate'),
)

SEESIONREFRESHER= (
    ('uac', 'uac'),
    ('uas', 'uas'),
)

SENDRPID= (
    ('yes', 'yes'),
    ('no', 'no'),
)

REGISTERTRYING= (
    ('yes', 'yes'),
    ('no', 'no'),
)

CONSTANTSSRC= (
    ('yes', 'yes'),
    ('no', 'no'),
)

USEREQPHONE= (
    ('yes', 'yes'),
    ('no', 'no'),
)

TEXTSUPPORT= (
    ('yes', 'yes'),
    ('no', 'no'),
)

FAXDETECT= (
    ('yes', 'yes'),
    ('no', 'no'),
)

BUGGYMWI= (
    ('yes', 'yes'),
    ('no', 'no'),
)

CALLINGPRES= (
    ('allwoed_not_screened', 'allwoed_not_screened'),
    ('allwoed_passed_screen', 'allwoed_passed_screen'),
    ('allowed_failed_screen', 'allowed_failed_screen'),
    ('allowed', 'allowed'),
    ('prohib_not_screened', 'prohib_not_screened'),
    ('prohib_passed_screen', 'prohib_passed_screen'),
    ('prohib_failed_screen', 'prohib_failed_screen'),
    ('prohib', 'prohib'),
)

HASVOICEMAIL= (
    ('yes', 'yes'),
    ('no', 'no'),
)

SUBSCRIBEMWI= (
    ('yes', 'yes'),
    ('no', 'no'),
)

AUTOFRAMING= (
    ('yes', 'yes'),
    ('no', 'no'),
)

G726NONSTANDARD= (
    ('yes', 'yes'),
    ('no', 'no'),
)

IGNORESDPVERSION= (
    ('yes', 'yes'),
    ('no', 'no'),
)

ALLOWTRANSFER= (
    ('yes', 'yes'),
    ('no', 'no'),
)

DYNAMIC= (
    ('yes', 'yes'),
    ('no', 'no'),
)
