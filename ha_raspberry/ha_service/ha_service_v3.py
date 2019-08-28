from requests import post,get
import paho.mqtt.client as mqtt
import json, configparser

config = configparser.ConfigParser()
config.read("ha_service")

# MQTT
MQTT_SERVER = config.get("MQTT", "MQTT_SERVER")
MQTT_PORT = config.get("MQTT", "MQTT_PORT")
MQTT_CONN_SEC = config.get("MQTT", "MQTT_CONN_SEC")
MQTT_PATH = config.get("MQTT", "MQTT_PATH")
USER_NAME = config.get("MQTT", "USER_NAME")
PWD = config.get("MQTT", "PWD")

# CLIEMT
CLIENT_NAME = config.get("CLIENT", "CLIENT_NAME")
CLIENT_IP = config.get("CLIENT", "CLIENT_IP")
CLIENT_PORT = config.get("CLIENT", "CLIENT_PORT")

# HOMEASSISTANT
TOKEN = config.get("HOMEASSISTANT", "TOKEN")
HO = config.get("HOMEASSISTANT", "HO")
DONG = config.get("HOMEASSISTANT", "DONG")
IP_ADDR = config.get("HOMEASSISTANT", "IPADDR")
ULPK = config.get("HOMEASSISTANT", "ULPK")

class HomeassistantService:
    def __init__(self, token):
        self.url = 'http://%s:8123/api' % (IP_ADDR)
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'authorization': 'Bearer %s' % (token)
        }

    def service(self, domain, service, entity, client):
        url = self.url+"/services" + '/' + domain + '/' + service
        post_result = json.loads(post(url, headers=self.headers, data=json.dumps(entity)).text)

        if len(post_result) > 1:
            for result in post_result:
                if entity['entity_id'] == result['entity_id']:
                    return dict({"success": True, "clientId": client,"data" :  result})
        else:
            return dict({"success": True, "clientId": client, "data" :  post_result})

    def data(self, apiUrl, httpMethod, serviceData, clientId):
        url = self.url + "/" + apiUrl
        print(url)
        print(self.headers)
        if httpMethod == "GET":
            return dict({"success": True, "clientId": clientId, "data": get(url, headers=self.headers).text})

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    print(MQTT_PATH+ULPK+"/#")
    client.subscribe(MQTT_PATH+ULPK+"/#")

def on_message(client, userdata, msg):
    data = json.loads(str(msg.payload.decode("utf-8", "ignore")))
    check_list = ['messageType', 'tit', 'message', 'time', 'usrPk', 'isShowMsg', 'domain', 'service', 'apiUrl', 'uidList', 'resvdate']
    if data["messageType"] == "COMMAND":
        res = homeassistantService.service(data['domain'], data['service'], data['serviceData'], data['clientId'])

        if(data["service"] == "close_cover"):
            res["data"] = {"state":"open"}
        elif (data["service"] == "open_cover"):
            res["data"] = {"state": "close"}

    elif data["messageType"] == "DATA":
        res = homeassistantService.data(data['apiUrl'], data['httpMethod'], data['serviceData'], data['clientId'])

    data['ulPk'] = int(ULPK)
    data['test'] = "yun"

    for i in check_list:
        if i in data.keys():
            res[i] = data[i]
        else:
            res[i] = ""

    print(data)
    print(res)
    print(json.dumps(res))
    mqttc = mqttc_info()
    mqttc.publish("hasensor_message/"+ data["usrPk"]+ "/" + HO + "/" + DONG, json.dumps(res))

    url = ('https://jiot.iotjiguem.com/api/' + data['returnUrl'])
    headers = {
        'Content-Type': 'application/json'
    }
    res = post(url
               , headers=headers
               , data= json.dumps(res)
               ) # --> 문자열로 보내주세요~
    print(res.status_code)

def mqttc_info():
    mqttc = mqtt.Client(CLIENT_NAME)
    mqttc.username_pw_set(USER_NAME, PWD)
    mqttc.connect(CLIENT_IP, int(CLIENT_PORT))
    mqttc.loop(5)
    return mqttc

if __name__ == "__main__":
    homeassistantService = HomeassistantService(TOKEN)

    client = mqtt.Client()
    client.username_pw_set(USER_NAME, PWD)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_SERVER, 1883, 60)
    client.loop_forever()
