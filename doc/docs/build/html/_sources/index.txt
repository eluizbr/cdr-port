Bem-Vindo a documentação do CDR-port!
=====================================



CDR-port é uma apliacação desenvolvida em Python utilizando o Framework
Django, que tem como objetivo, criar uma interface CDR (Call Detail Reports) 
para Asterisk nas versões 1.8.X, 10.X, 11.X, 12.X .


Quem deve utilizar?
-------------------

Toda e qualquer empresa e ou profissionais que desejam ter sistema de relátorios
para telefonia objetivo.


Instalação
-----------

CDR-port é uma aplicação baseada em Django, e para a versão FRRE, 
será necessário instalar as seguintes dependências:


    - python >= 2.6
    - Nginx
    - Django Framework >= 1.7


Todas as dependências podem ser facilmente instaladas usando o PIP:

    - https://github.com/cdr-port/cdr-port/blob/master/install/requirements.txt


Script de instalação
~~~~~~~~~~~~~~~~~~~~

Temos um script para instalação automadizada do CDR-port. 


    - wget https://github.com/cdr-port/cdr-port/raw/master/install/setup.sh


Documentation
-------------

Complete documentation :

    - http://docs.newfies-dialer.org/


Screenshot
----------

* Customer Frontend :

    http://localhost:8000/
    This application provides a User interface for restricted management of
    the User's Campaign, Phonebook, Subscriber. It also provides detailed
    Reporting of calls and message delivery.

.. image:: https://github.com/Star2Billing/newfies-dialer/raw/develop/docs/source/_static/images/customer_screenshot.png


* Dashboard Frontend :

    http://localhost:8000/dashboard/
    Newfies-Dialer Dashboard provides a contact and call reporting for the running campaign.

.. image:: https://github.com/Star2Billing/newfies-dialer/raw/develop/docs/source/_static/images/newfies-dialer-dashboard.png


* Admin Dashboard :

    http://localhost:8000/admin/
    This interface provides user (ACL) management, a full control of all
    Campaigns, Phonebooks, Subscribers, Gateway, configuration of the
    Audio Application.

.. image:: https://github.com/Star2Billing/newfies-dialer/raw/develop/docs/source/_static/images/admin_screenshot.png


Additional information
-----------------------

* Fork the project on GitHub : https://github.com/Star2Billing/newfies-dialer

* License : MPL 2.0 (https://raw.github.com/Star2Billing/newfies-dialer/master/COPYING)

* Official website : http://www.newfies-dialer.org

* `Google Group`_ - the mailing list is newfies-dialer@googlegroups.com

* `Forum`_

* `Continuous integration homepage`_ on `travis-ci.org`_

* `Twitter account for news and updates`_

.. _`Google Group`: https://groups.google.com/forum/?fromgroups#!forum/newfies-dialer
.. _`Forum`: http://forum.newfies-dialer.org/
.. _`Continuous integration homepage`: http://travis-ci.org/#!/Star2Billing/newfies-dialer
.. _`travis-ci.org`: http://travis-ci.org/
.. _`Twitter account for news and updates`: https://twitter.com/newfies_dialer


Support
-------

The Newfies-Dialer project is supported by Star2billing S.L.
For more information, see http://www.newfies-dialer.org/

Please email us at newfies-dialer@star2billing.com for more information


