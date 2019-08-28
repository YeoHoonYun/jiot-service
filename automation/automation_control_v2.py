import requests, datetime, pprint, json, time
from pytz import timezone
from requests import post
import threading

# ip_add = "localhost"
ip_add = "183.98.179.130"
https_ip_add = "https://jiot.iotjiguem.com"
uri = "/api"

full_add = https_ip_add + uri

# device_url = "http://%s:8081/devicecontrol/messageTest" % (ip_add)
device_url = "%s/devicecontrol/message" % (full_add)

headers = {
    'Content-Type': "application/json",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
}
class AsyncTask:
    def __init__(self):
        pass

    def device_control(self, service):
        url = '%s/devicecommand/publishcommand' % (full_add)
        headers = {
            'Content-Type': 'application/json'
        }
        service["domain"] =  service["deviceDomain"]
        service["httpMethod"] = "POST"
        service["messageType"] = "COMMAND"
        service["service"] = service["deviceService"]
        service["isShowMsg"] = service["isShowMsg"]
        service["serviceData"] =  json.loads(service["deviceData"])
        print(json.dumps(service))
        #
        # result = post(url
        #            , headers=headers
        #            , data=json.dumps(service)
        #            ).text
        # result = json.loads(result)

    def recomend_msg(self, service):
        url = "%s/device1" % (https_ip_add)
        headers = {
            'Content-Type': 'application/json'
        }
        service["userId"] = service["usrPk"]
        result = post(url
                   , headers=headers
                   , data=json.dumps(service))

    def get_kst(self, fmt):
        KST = datetime.datetime.now(timezone('Asia/Seoul'))
        return KST.strftime(fmt)

    def device_automation(self):
        threading.Timer(1, self.device_automation).start()
        resvdate = self.get_kst("%Y-%m-%d")
        time = self.get_kst("%H:%M:%S")

        data = {
            "resvdate" : resvdate,
            "time" : time
        }
        print(resvdate + " " + time)

        # response = json.loads(requests.request("GET", device_url, headers=headers).text)
        response = json.loads(requests.request("POST", url=device_url, data=json.dumps(data), headers=headers).text)
        if len(response) == 0:
            print("pass")
        else:
            for data in response:
                uidList = []
                # pprint.pprint(data)
                if (data.get("isGroupMsg")):
                    print("isShowMsg")
                    userUid = json.loads(requests.request("GET", "%s/user/getUsers/%s" % (full_add, data.get("userModel").get("usrpk")), headers=headers).text)
                else:
                    userUid = data.get("userModel").get("usruid")
                uidList.append(userUid)

                data["usrPk"] = data.get("userModel").get("usrpk")
                data["isAuto"] = data.get("userModel").get("isAuto")

                if data.get("isAuto") == False:
                    data["msgTyp"] == 103003

                del data["userModel"]

                pprint.pprint(data)

                data["test"] = "yun"
                data['uidList'] = uidList
                data["resvdate"] = resvdate
                data["time"] = time

                pprint.pprint(data)

                if data["msgTyp"] == 103001:
                    print("디바이스 제어")
                    # self.device_control(service=data)

                elif data["msgTyp"] == 103002 or data["msgTyp"] == 103003:
                    print("추천")
                    self.recomend_msg(service=data)

if __name__ == '__main__':
    at = AsyncTask()
    at.device_automation()