import getpass
import telnetlib


def device_login():
    Host = "192.168.184.128"
    username = 'admin'
    password = getpass.getpass()
    tn = telnetlib.Telnet(Host)

    tn.read_until(b'Username:')
    tn.write(username.encode('ascii') + b"\n")
    if password:
        tn.read_until(b'Password')
        tn.write(password.encode('ascii') + b"\n")
    return tn

def device_logout(tn_obj):
    output = tn_obj.read_all().decode("ascii")
    return output

