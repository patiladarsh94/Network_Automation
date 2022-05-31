from netmiko import ConnectHandler
R1 = '192.168.29.13'
R2 = '192.168.29.58'
R3 = '192.168.29.230'

username ='admin'
password = 'cisco'

devices = [R1, R2, R3]

for device in devices:
    device_dict = {
        'device_type' : 'cisco_ios',
        'ip' : device,
        'username' : username,
        'password' : password
    }

    ssh = ConnectHandler(**device_dict)

    print("SSH established with " + device)

    interface_brief = ssh.send_command("show ip interface brief")
    print(interface_brief)