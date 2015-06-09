# -*- coding: UTF-8 -*-
import argparse
import requests
import json
import sqlite3
import os


url = "https://www.cloudflare.com/api_json.html"
site = "cdr-port.net"
mail = "eluizbr@gmail.com"


def database_registry(dns_id, name, result):
    conn = sqlite3.connect("dns_records.s3db")
    cursor = conn.cursor()

    strsql = """
        insert into dns_records (dns_id, name, result) values
        ('%s', '%s', '%s')
    """ % (dns_id, name, result)

    cursor.execute(strsql)
    conn.commit()


def get_dns_to_delete(name):
    conn = sqlite3.connect('dns_records.s3db')
    cur = conn.cursor()

    strsql = """
        select dns_id from dns_records where name = '%s'
    """ % name

    cur.execute(strsql)
    for c in cur:
        if c != '':
            return c
        else:
            raise ValueError("Dns id not found!")


def register_new(name, token, operation):
    """
        Required libs: requests
        pip install requests

        Sample of calls:
        Create: python dns_update.py somevirtualhost token create ''

        name: somevirtualhost
        token: complete path to the file with token info
        operation: create
        dns_id: have to pass an empty string :(

        Delete: python dns_update.py 'nameofdns' token delete

        name: Empty string as the name is not needed to delete
        token: complete path to the file with token info
        operation: delete
        dns_id: Id of dns record created in CloudFlare

        Parameters that are the same to both operations are fixed in parameters variable.
        Other parameters are added to dict as/only if they are needed ;)

    """

    # Criando database...
    if not os.path.isfile('dns_records.s3db'):
        conn = sqlite3.connect("dns_records.s3db")
        cursor = conn.cursor()
        strsql = ("""
                create table dns_records (dns_id, name, result)
            """)
        cursor.execute(strsql)
        conn.commit()

    parameters = {
        'email': mail,
        'z': site,
        'type': 'A',
        'content': '177.52.104.53',
        'ttl': 120,
    }

    try:
        f = open(token, 'r')
        parameters['tkn'] = f.readline()

        if operation == 'create':
            parameters['a'] = 'rec_new'
            parameters['name'] = name
        else:
            parameters['a'] = 'rec_delete'
            parameters['id'] = get_dns_to_delete(name)

        r = requests.post(url, data=parameters)
        result = json.loads(r.text)

        print "Registered: %s " % result['result']
        print "DNS ID: %s " % result['response']['rec']['obj']['rec_id']
        print "Name: %s" % name

        if result['result'] == 'success':
            database_registry(
                result['response']['rec']['obj']['rec_id'], name, result['result'])

    except Exception, e:
        print e


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "name", help="Name to be used in the virtualhost", type=str)
    parser.add_argument(
        "token", help="Absolute path to the file containg the  api token", type=str)
    parser.add_argument(
        "operation", help="--c: Create new record; --d Delete existing record", type=str)
    # parser.add_argument(
    #     "dns_id", help="Dns id returned by cloudflare", type=str, default='')

    args = parser.parse_args()
    register_new(args.name, args.token, args.operation)  # , args.dns_id)
