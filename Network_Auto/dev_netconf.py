from ncclient import manager
import xmltodict
import pprint
from xml.dom.minidom import parseString
xe = {
    'host' : 'sandbox-iosxe-recomm-1.cisco.com',
    'port' : '830',
    'username' : 'developer',
    'password': 'C1sco12345',
    'hostkey_verify' : False
}

netconf = manager.connect(**xe)
running_config = netconf.get_config(source = 'running')
pretty_running = parseString(running_config.xml).toprettyxml()

# my_dict = xmltodict.parse(pretty_running)
# for key,value in my_dict.items():
#     print(key, value)
print(pretty_running)