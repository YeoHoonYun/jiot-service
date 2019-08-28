from requests import post,get
import paho.mqtt.client as mqtt
import json,pprint, requests

class HomeassistantService:
    def __init__(self):
        self.url = 'http://172.30.1.36:8123/api'
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0Njg4ZjcyNmI1OTM0ZWMyOTI5Nzg3OTYxOTkxYTliYSIsImlhdCI6MTU1MzA0NDA0MywiZXhwIjoxODY4NDA0MDQzfQ.L8w6WlZOjqpLG5ezIkkEPM_EQXayPBpgQHk6fJSv5aY'
        }
        self.error_list = ['404: Not Found']

    def service(self, domain, service, entity, client):
        try:
            url = self.url+"/services" + '/' + domain + '/' + service
            post_result = json.loads(post(url, headers=self.headers, data=json.dumps(entity)).text)

            # 리턴값 에러
            for error in self.error_list:
                if error in post_result:
                    return dict({"success": False, "clientId": client,"data" : "" ,"error" : error})

            # entity_id 검색
            if len(post_result) > 1:
                for result in post_result:
                    # print(entity['entity_id'] == result['entity_id'])
                    if entity['entity_id'] == result['entity_id']:
                        # print(result)
                        return dict({"success": True, "clientId": client,"data" :  result})
            else:
                return dict({"success": True, "clientId": client, "data" :  post_result})

        except:
            return dict({"success": False, "clientId": client, "data" : "" , "error" : 'System Error'})

    def data(self, apiUrl, httpMethod, serviceData, clientId):
        url = self.url + "/" + apiUrl
        if httpMethod == "GET":
            return dict({"success": True, "clientId": clientId, "data": get(url, headers=self.headers).text})

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    data = json.loads(str(msg.payload.decode("utf-8", "ignore")))
    check_list = ['messageType', 'tit', 'message', 'time', 'usrPk', 'isShowMsg', 'ulPk', 'sid']
    #print(data)
    try:
        #print(data)
        if data["messageType"] == "COMMAND":
            res = homeassistantService.service(data['domain'], data['service'], data['serviceData'], data['clientId'])
            res["domain"] = data['domain']
            res["service"] = data['service']

            if(res["service"] == "close_cover"):
                res["data"] = {"state":"open"}
            if (res["service"] == "open_cover"):
                res["data"] = {"state": "close"}

        elif data["messageType"] == "DATA":
            #print(data)
            res = homeassistantService.data(data['apiUrl'], data['httpMethod'], data['serviceData'], data['clientId'])
            res["apiUrl"] = data["apiUrl"]
            print(data)

        for i in check_list:
            if i in data.keys():
                res[i] = data[i]
            else:
                res[i] = ""

        #res["messageType"] = data["messageType"]
        #res["tit"] = data["tit"]
        #res["message"] = data["message"]
        #res["time"] = data["time"]
        #res["usrPk"] = data["usrPk"]
        #res["isShowMsg"] = data["isShowMsg"]
        print(data)

        mqttc = mqttc_info()
        mqttc.publish("hasensor_message/"+ data["usrPk"]+ "/" + ho + "/" + dong, json.dumps(res))

        print(data)

        url = 'http://jiot.jiguem.com:8081/api/' + data['returnUrl']
        headers = {
            # 'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        res = post(url
                   , headers=headers
                   , data= json.dumps(res)
                   ) # --> 문자열로 보내주세요~
        print(url)
        #print(res)
        
    except Exception as ex:
        print(ex + "test")

def mqttc_info():
    mqttc = mqtt.Client(client_name)
    mqttc.username_pw_set('jiguem', 'jigeum!')
    mqttc.connect(client_ip, client_port)
    #mqttc.loop(5)
    return mqttc

if __name__ == "__main__":
    homeassistantService = HomeassistantService()
    
    # 서비스 명령어 받는 주소
    client = mqtt.Client()
    MQTT_SERVER = "jiot.jiguem.com"
    MQTT_PATH = "jiot/#"
    USER_NAME = "jiguem"
    PWD = "jigeum!"

    # 실행 로그 전달
    client_name = "python_pub"
    client_ip = "jiot.jiguem.com"
    client_port = 1883
    ho = "406"
    dong = "503"

    client.username_pw_set(USER_NAME, PWD)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_SERVER, 1883, 60)

    client.loop_forever()
