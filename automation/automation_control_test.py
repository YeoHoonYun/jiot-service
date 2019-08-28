import requests, datetime, pprint, json, time
from pytz import timezone
from requests import post

ip_add = "localhost"
# ip_add = "183.98.182.142"

def device_control(service):
    pass
    # url = 'http://jiot.jiguem.com:8081/api/devicecommand/publishcommand'
    # headers = {
    #     'Content-Type': 'application/json'
    # }
    #
    # data = {
    #     "time" : service["time"],
    #     "usrPk": service["usrPk"],
    #     "domain": service["deviceDomain"],
    #     "httpMethod": "POST",
    #     "messageType": "COMMAND",
    #     "service": service["deviceService"],
    #     "serviceData": json.loads(service["deviceData"]),
    #     "tit": service["tit"],
    #     "message": service["message"],
    #     "isShowMsg" : service["isshowmsg"]
    # }
    # pprint.pprint(data)
    # result = post(url
    #            , headers=headers
    #            , data=json.dumps(data)
    #            ).text
    # result = json.loads(result)

def recomend_msg(service):
    pass
    # url = "http://demo.jiguem.com:5003/device1"
    # headers = {
    #     'Content-Type': 'application/json'
    # }
    # pprint.pprint(json.dumps(service))
    # service["userId"] = service["usrPk"]
    # result = post(url
    #            , headers=headers
    #            , data=json.dumps(service))

def get_kst(fmt):
    KST = datetime.datetime.now(timezone('Asia/Seoul'))
    return KST.strftime(fmt)

if __name__ == '__main__':
    device_url = "http://%s:8081/devicecontrol/messageTest" % (ip_add)
    headers = {
        'Content-Type': "application/json",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
    }
    resvdate_ = get_kst("%Y-%m-%d")
    time_ = get_kst("%H:%M:%S")

    response = json.loads(requests.request("GET", device_url, headers=headers).text)

    for data in response:
        ulPk = json.loads(requests.request("GET", "http://%s:8081/user/getLoc/%s" % (ip_add, data['usrPk']), headers=headers).text)["ulPk"]
        user_url = "http://%s:8081/user/getUsers/%s"% (ip_add, ulPk)
        usrUidList = json.loads(requests.request("GET", user_url, headers=headers).text)

        data['ulPk'] = ulPk
        data['uidList'] = usrUidList
        data["resvdate"] = get_kst("%Y-%m-%d")
        data["time"] = get_kst("%H:%M:%S")

        pprint.pprint(data)

        if data["msgTyp"] == 103001:
            print("디바이스 제어")

        elif data["msgTyp"] == 103002 or data["msgTyp"] == 103003:
            print("추천")