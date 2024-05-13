import requests 
import xmltodict
import json
from namecheap import Api

import untangle

API_USER = 'Avisagat'
API_KEY = '6b53bf150dff4b13a49aaf197f1237c2'
IP_ADDRESS = '110.227.20.239'
API_USER = 'Avisagat'

api = Api(API_USER, API_KEY,API_USER,IP_ADDRESS, sandbox = True, debug=True)

def domain_available():
    domain_name = "google.com"
    return api.domains_check(domain_name)



def register_domain():
    domain_name = 'avinash.bot'
    api.domains_create(
        DomainName=domain_name,
        FirstName='avi',
        LastName='sagat',
        Address1='xyxz',
        City='Pune',
        StateProvince='Pune',
        PostalCode='411043',
        Country='India',
        Phone='+91.123456677',
        EmailAddress='xyz@xyx.com'
    )
    
    return domain_name


def domains_getList():
    list_ = (api.domains_getList())
    for i in list_:
        print(i)
    return list_

print(domains_getList())