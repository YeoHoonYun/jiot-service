from requests import post
from pytz import timezone
import json, datetime, time, pprint

def device_control(service):
    url = 'http://jiot.jiguem.com:8081/api/devicecommand/publishcommand'
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        "time" : service["time"],
        "usrPk": service["usrPk"],
        "domain": service["deviceDomain"],
        "httpMethod": "POST",
        "messageType": "COMMAND",
        "service": service["deviceService"],
        "serviceData": json.loads(service["deviceData"]),
        "tit": service["tit"],
        "message": service["message"],
        "isShowMsg" : service["isshowmsg"]
    }
    pprint.pprint(data)
    result = post(url
               , headers=headers
               , data=json.dumps(data)
               ).text
    result = json.loads(result)

def recomend_msg(service):
    url = "http://demo.jiguem.com:5002/device1"
    headers = {
        'Content-Type': 'application/json'
    }
    pprint.pprint(json.dumps(service))
    service["userId"] = service["usrPk"]
    result = post(url
               , headers=headers
               , data=json.dumps(service)
            )

def get_kst(fmt):
    # fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    # fmt = "%Y-%m-%d %H:%M:%S"
    KST = datetime.datetime.now(timezone('Asia/Seoul'))
    return KST.strftime(fmt)


def main():
    # pprint.pprint(service)
    if service["msgtyp"] == 103001:
        print("디바이스 제어")
        device_control(service)

    elif service["msgtyp"] == 103002:
        print("추천")
        recomend_msg(service)
    else:
        pass
    if (service["interv"]):
        print(service["interv"])
        # time.sleep(service["interv"])


if __name__ == "__main__":
    demo_flag = True
    url = 'http://jiot.jiguem.com:8081/api/device/getdevicecontrolmessages'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
      "outCond": 1,
      "statCode": 1,
      "usrCodes": [5]
    }

    ret = post(url
               , headers=headers
               , data=json.dumps(data)
               ).text
    services = json.loads(ret)
    pprint.pprint(services)

    # TODO 메시지 타입별로 처리해주는 방법이 다르다.
    # TODO 시간별로 실행하는 것을 따로 만든다.
    for service in services["data"]:
        service["usrPk"] = str(service["usrPk"])+":"
        # print(int(service["time"].replace(":","")) > int(get_kst("%H%M%S")))
        if(int(service["time"].replace(":","")) > int(get_kst("%H%M%S")) and not demo_flag):
            service_time = service["time"]
            print("설정 값 : " + service_time)
            while(True):
                print(get_kst("%H:%M:%S"))
                print(int(service["time"].replace(":","")) == int(get_kst("%H%M%S")))
                if(int(service["time"].replace(":","")) == int(get_kst("%H%M%S"))):
                    main()
                    break

        #데모
        else:
            main()