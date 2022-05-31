from distutils.command.config import config
from netmiko import ConnectHandler
import re
R1 = {
    'device_type' : 'cisco_ios',
    'ip' : '10.82.139.122',
    'username':'admin',
    'password':'cisco!123',
    'secret' : 'cisco!123',
}

conn = ConnectHandler(**R1)
print("Connection established")
ip = input('Enter ip add:')
mask = input('Enter mask:')

ip_add = 'ip address ' + ip + ' ' + mask
config_commands = ['int loopback 11', ip_add , 'no shut' ]

if not conn.check_enable_mode():
    conn.enable()
cfg = conn.send_config_set(config_commands)

print(cfg)



