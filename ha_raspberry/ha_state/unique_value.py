import netifaces, os, miniupnpc
import json, pprint
from requests import *

ulPk = "10001"
# dest = "183.98.182.142"
dest = "https://jiot.iotjiguem.com/api"
nic = "wlan0"

def getserial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"
    return cpuserial
if __name__ == '__main__':
    url = "%s/gateway/insertDeviceGateway" % (dest)
    headers = {
        'Content-Type': "application/json",
    }
    data = {
        "inDt": "2019-06-20T07:01:38.499Z",
        "macAddr": "00:13:ef:67:1a:d3",
        "priAddr": "172.30.1.38",
        "pubAddr": "125.131.126.177",
        "sno": "0000000063f638cc",
        "ulPk": int(ulPk)

    }

    ip_address = netifaces.ifaddresses(nic)

    public_address = get('https://api.ipify.org').text
    private_address = ip_address[netifaces.AF_INET][0]['addr']
    mac_address = ip_address[netifaces.AF_LINK][0]['addr']
    serial_number = getserial()

    data["sno"] = serial_number
    data["pubAddr"] = public_address
    data["priAddr"] = private_address
    data["macAddr"] = mac_address
    print(data)

    res = post(
        url=url,
        headers=headers,
        data=json.dumps(data)
    )

    print(res.text)

    # --------------------------------------------------------------------------------------------------------------

