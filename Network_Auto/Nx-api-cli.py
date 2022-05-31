import requests
import json

host  = "https://sandbox-nxos-1.cisco.com"
username = "admin"
password = "Admin_1234!"

requests.packages.urllib3.disable_warnings()


header = {"content-type": "application/json"}
showcmd = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show version",
    "output_format": "json"
  }
}

response = requests.post(host,data=json.dumps(showcmd),headers=header,auth=(username,password),verify=False)

print(response)