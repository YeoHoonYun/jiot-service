# import netifaces, miniupnpc
import json
import time

from requests import *
import threading

ip_addr = "14.47.102.251"
# dest = "183.98.182.142"
# dest = "https://jiot.iotjiguem.com/api"
dest = "http://localhost:8081/api"
ulPk = "10001"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0ZTQwZTYyN2IzMWI0OWE1YTViYmViZjU0NDk1ZTMzZSIsImlhdCI6MTU2NTU5MzgwNywiZXhwIjoxODgwOTUzODA3fQ.HIlYcI_eyI4I8-Gn28NGWmAyVunL6tECxaCX5nztXEM"
# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJiMzEwMWRhMjYxZmE0ZTNjODVhNTE4MTUyZDZjZDQ3ZiIsImlhdCI6MTU2NTU4ODcwOCwiZXhwIjoxODgwOTQ4NzA4fQ.bggPUunwH21FgrkADNkE_hK35iz58XA-92HvWHbTBaQ"
service_mode = False

class AsyncTask:
    def __init__(self):
        pass

    def device_state(self):
        threading.Timer(5, self.device_state).start()
        apiUri = "states"
        url = ("http://%s:8123/api/" + apiUri) % (ip_addr)
        dev_token = token
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'authorization': 'Bearer %s' % (dev_token)
        }

        res = dict({"success": True, "clientId": "", "data": get(url, headers=headers).text})
        res["apiUrl"] = apiUri
        res["httpMethod"] = "GET"
        res["messageType"] = "DATA"
        res["ulPk"] = ulPk

        url = '%s/device/savegatewaydevicedata' % (dest)
        headers = {
            'Content-Type': 'application/json'
        }

        # pprint.pprint(json.loads(res['data']))
        print(res)

        res = post(url
                   , headers=headers
                   , data=json.dumps(res)
                   )  # --> 문자열로 보내주세요~

        print(res.status_code)

if __name__ == '__main__':
    apiUri_list = ["states","services"]

    if(not service_mode):
        nic = "wlan0"
        # ip_addr = netifaces.ifaddresses(nic)
        # ip_addr = ip_addr[netifaces.AF_INET][0]['addr']

        for apiUri in apiUri_list:
            url = ("http://%s:8123/api/" + apiUri) % (ip_addr)
            dev_token = token
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'authorization': 'Bearer %s' % (dev_token)
            }

            res = dict({"success": True, "clientId": "", "data": get(url, headers=headers).text})
            res["apiUrl"] = apiUri
            res["httpMethod"] = "GET"
            res["messageType"] = "DATA"
            res["ulPk"] = ulPk

            url = '%s/device/savegatewaydevicedata' % (dest)
            headers = {
                'Content-Type': 'application/json'
            }

            # pprint.pprint(json.loads(res['data']))
            print(res)

            res = post(url
                       , headers=headers
                       , data=json.dumps(res)
                       )  # --> 문자열로 보내주세요~

            print(res.status_code)
            time.sleep(3)
    else:
        ip_addr = ip_addr
        at = AsyncTask()
        at.device_state()