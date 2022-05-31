from ncclient import manager
import xmltodict

xe = {
    'host' : 'sandbox-iosxe-recomm-1.cisco.com',
    'port' : '830',
    'username' : 'developer',
    'password': 'C1sco12345',
    'hostkey_verify' : False
}

netconf = manager.connect(**xe)

payload = '''
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{interface}</name>
            <description>{description} </description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:{type}</type>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>{ip}</ip>
                        <netmask>{mask}</netmask>
                    </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
'''
int_type = input("Enter the interface type Physical/Logical : ")
if int_type.lower() == 'physical':
    type = "ethernetCsmacd"
elif int_type.lower() == 'logical':
    type = "softwareLoopback"
else:
    print("Invalid interface type")
interface = input("Enter the interface name : ")
description = input("Enter the description : ")
ip = input("Enter the ip : ")
mask = input("Enter the mask : ")

interface_payload = payload.format(
    interface = interface,
    description = description,
    ip = ip,
    mask = mask,
    type = type
)
interface_config = netconf.edit_config(interface_payload, target = 'running')
print(interface_config)