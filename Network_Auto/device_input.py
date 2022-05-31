import re
import base

tn = base.device_login()

user_choice = input("Enter the choice..\n 1. Interface Configuration\n 2. /Static route configuration\n. Your choice : ")
if user_choice == '1':
    int_name = input("Enter the interface name : ")
    int_ip = input("Enter the Interface IP address : ")
    int_mask = input("Enter your Subnet Mask : ")
    commands = """
    configure terminal
    interface {name}
    description Configured using Automation
    ip address {ip} {mask}
    no shut
    end
    exit
    """.format(name = int_name,ip = int_ip,mask = int_mask)
    tn.write(commands.encode("ascii"))
    print(base.device_logout(tn))
elif user_choice == '2':
    Nw_id = input("Enter the Network ID : ")
    mask = input("Enter the Network Mask : ")
    next_hop = input("Enter the next hop : ")
    command = "conf t\n ip route {network} {mask} {next_hop} \n end \n".format(network = Nw_id,mask = mask, next_hop = next_hop)
    print(command)
    tn.write(command.encode("ascii"))
    print(base.device_logout(tn))
    

