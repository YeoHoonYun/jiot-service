import paho.mqtt.client as mqtt
from requests import get
import json, configparser
from sseclient import SSEClient

config = configparser.ConfigParser()
config.read("ha_gateway")

# HOMEASSISTANT
TOKEN = config.get("HOMEASSISTANT", "TOKEN")
ULPK = config.get("HOMEASSISTANT", "ULPK")
HO = config.get("HOMEASSISTANT", "HO")
DONG = config.get("HOMEASSISTANT", "DONG")
IP_ADDR = config.get("HOMEASSISTANT", "IPADDR")

# 기본 필드 설정
CLIENT_NAME = config.get("CLIENT", "CLIENT_NAME")
CLIENT_IP = config.get("CLIENT", "CLIENT_IP")
CLIENT_PORT = config.get("CLIENT", "CLIENT_PORT")
USER_NAME = config.get("CLIENT", "USER_NAME")
PWD = config.get("CLIENT", "PWD")

def pubData(mqttc,topic_pre, topic, data, ho, dong):
    data['ulPk'] = int(ULPK)
    data['test'] = "yun"
    print(topic_pre + topic + "/" + ho + "/"+dong)
    try:
        mqttc.publish(topic_pre + topic + "/" + ho + "/"+dong, json.dumps(data))
    except Exception as ex:
        print("Exception: {}".format(ex))
        mqttc.publish(topic_pre + topic + "/" + ho + "/" + dong, json.dumps(data))

def start(entity_list, auth):
    while(True):
        messages = SSEClient('http://%s:8123/api/stream'  % (IP_ADDR), headers=auth)
        for msg in messages:
            mqttc = mqttc_info()
            msg = msg.__dict__
            if (msg["data"] != "ping"):
                print(entity_list)
                for entity in entity_list:
                    if (entity in msg["data"]):
                        if ("state_changed" in json.loads(msg["data"])["event_type"]):
                            pubData(mqttc,"hasensor/", entity, json.loads(msg["data"])["data"]["new_state"], HO, DONG)
                            print("mqtt publish success")
                        else:
                            print("****************************************")
                            print("event_type / etc.....")
                            pubData(mqttc, "haservice/", entity, json.loads(msg["data"]), HO, DONG)
                            print("****************************************")


def mqttc_info():
    mqttc = mqtt.Client(CLIENT_NAME)
    mqttc.username_pw_set(USER_NAME, PWD)
    mqttc.connect(CLIENT_IP, int(CLIENT_PORT))
    return mqttc

# def getAccessToken():
#     url = 'http://172.30.1.38:8123/auth/token'
#     headers = {
#         'Content-Type': 'application/x-www-form-urlencoded'
#     }
#     data = {
#         'client_id': 'http://172.30.1.38:8123/',
#         'grant_type': 'refresh_token',
#         'refresh_token': 'd70971081e33eaac700dd1e596d69dc4351fc0c5248bc88b794216a8cb5bed0aeba2b50d9ea5baafac239de886093ed0e422d29e6d6e29f2ead88dac03a7394d'
#     }
#     return json.loads(post(url, headers=headers, data=data).text)['access_token']

if __name__ == "__main__":
    # token = getAccessToken()
    url = "https://jiot.iotjiguem.com/api/device/getdevices/%s" % (int(ULPK))
    headers = {
        'Content-Type': 'application/json'
    }

    res = get(
        url = url,
        headers = headers
    )

    entity_list = [x["devnm"] for x in json.loads(res.text)["data"]]
    auth = {'Authorization': 'Bearer ' + TOKEN}

    try:
        start(entity_list, auth)
    except:
        start(entity_list, auth)