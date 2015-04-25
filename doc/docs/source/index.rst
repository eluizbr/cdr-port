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

* Dashboard :

    http://localhost:8000/
    This application provides a User interface for restricted management of
    the User's Campaign, Phonebook, Subscriber. It also provides detailed
    Reporting of calls and message delivery.

.. image:: https://raw.githubusercontent.com/eluizbr/cdr-port/devel/cdr/img/dashborad.png


* Dashboard Resumos :

    http://localhost:8000/dashboard/
    Newfies-Dialer Dashboard provides a contact and call reporting for the running campaign.

.. image:: https://raw.githubusercontent.com/eluizbr/cdr-port/devel/cdr/img/dashboar-2.png


* CDR Versão FREE :

    http://localhost:8000/admin/
    This interface provides user (ACL) management, a full control of all
    Campaigns, Phonebooks, Subscribers, Gateway, configuration of the
    Audio Application.

.. image:: https://raw.githubusercontent.com/eluizbr/cdr-port/devel/cdr/img/cdr-free.png


* CDR Versão PREMIUM :

	O CDR-port é totalmente integrado como sistema de portabilidade. A base fica 100% local,
	Não é necessário consultas pela internet.

.. image:: https://raw.githubusercontent.com/eluizbr/cdr-port/devel/cdr/img/cdr-premium-2.png

