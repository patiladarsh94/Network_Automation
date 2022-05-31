import json
import requests
from requests.auth import HTTPBasicAuth


interface_payload = {
    'ietf-interfaces:interface': {
        "name": "Loopback1406",
        "description": "Added with RESTCONF on May-30-2022",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "1.2.3.6",
              "netmask": "255.255.255.255"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      }   
}
# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()


# credentials to access the Sandbox
host = 'sandbox-iosxe-latest-1.cisco.com'
user = 'developer'
password = 'C1sco12345'

# url string to issue GET request
xe_url = "https://{h}/restconf/data/ietf-interfaces:interfaces".format(h=host)

# RESTCONF media types for REST API headers
headers = {'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'}
        
# performs a GET on the specified url
config  = requests.post(url=xe_url, auth=(user, password),headers=headers, data=json.dumps(interface_payload), verify=False)
response = requests.get(xe_url, auth=(user, password),headers=headers, verify=False)

# print the json that is returned
dict_intf = json.loads(response.text)

list_intf = dict_intf['ietf-interfaces:interfaces']['interface']

for intf_dict in list_intf:
    if 'Loopback1406' in intf_dict['name']:
        print(intf_dict['name'], ': ', intf_dict['ietf-ip:ipv4']['address'][0]['ip'])
