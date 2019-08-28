import paho.mqtt.client as mqtt
from requests import get, post
import json, pprint, datetime, time
from sseclient import SSEClient

utctime = datetime.datetime.utcnow()
# 기본 필드 설정
client_name = "python_pub"
client_ip = "jiot.jiguem.com"
client_port = 1883
ho = "406"
dong = "503"

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

def pubData(mqttc,topic_pre, topic, data, ho, dong):
    data['ulPk'] = 1
    data['dt'] = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    pprint.pprint(data)
    print(topic_pre + topic + "/" + ho + "/"+dong)
    try:
        mqttc.publish(topic_pre + topic + "/" + ho + "/"+dong, json.dumps(data))
    except Exception as ex:
        print("Exception: {}".format(ex))
        mqttc.publish(topic_pre + topic + "/" + ho + "/" + dong, json.dumps(data))

def mess(msg):
    try:
        mqttc = mqttc_info()
        msg = msg.__dict__
        if (msg["data"] != "ping"):
            for entity in entity_list:
                if (entity in msg["data"]):
                    if ("state_changed" in json.loads(msg["data"])["event_type"]):
                        # pubData(mqttc,"hasensor/", entity, json.loads(msg["data"])["data"]["new_state"], ho, dong)
                        print("mqtt publish success")
                    else:
                        print("****************************************")
                        print("event_type / etc.....")
                        pprint.pprint(json.loads(msg["data"]))
                        pubData(mqttc, "haservice/", entity, json.loads(msg["data"]), ho, dong)
                        print("****************************************")
    except Exception as ex:
        print("Exception: {}".format(ex))

def start():
    while(True):
        messages = SSEClient('http://172.30.1.38:8123/api/stream', headers=auth)
        for msg in messages:
            mess(msg)


def mqttc_info():
    mqttc = mqtt.Client(client_name)
    mqttc.username_pw_set('jiguem', 'jigeum!')
    mqttc.connect(client_ip, client_port)
    #mqttc.loop(5)
    return mqttc

if __name__ == "__main__":
    ulpk = 1
    url = "http://jiot.jiguem.com:8081/api/device/getdevices?ulpk=%s" % ulpk
    headers = {
        'Content-Type': 'application/json'
    }

    res = get(
        url, headers
    )
    #TODO 동호수 매칭해서 가져올 수 있도록
    entity_list = [x["devnm"] for x in json.loads(res.text)["data"]]

    # entity_list = [
    #     'binary_sensor.door_window_sensor'
    #     , 'binary_sensor.motion_sensor'
    #     , 'cover.curtain'
    #     , 'light.gateway_light'
    #     # , 'light.geosil'
    #     , 'light.hue_color_lamp'
    #     , 'sensor.fibaro_illuminance'
    #     , 'sensor.fibaro_motion'
    #     , 'sensor.fibaro_tamper'
    #     , 'sensor.fibaro_temperature'
    #     , 'binary_sensor.switch'
    #     , 'fan.xiaomi_miio_device'
    # ]

    # token = getAccessToken()
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJlNzA5OGJiYTYxOTQ0ODU0ODg1MGJmNjYwYzhkODM0MyIsImlhdCI6MTU1NTQ3NzMxNCwiZXhwIjoxODcwODM3MzE0fQ.pHG-7BCkwDYOdidbNR24w7FUCFTXAH-Kr07_C3c6qKs'
    auth = {'Authorization': 'Bearer ' + token}
    # messages = None
    try:
        start()

    except Exception as ex:
        print("Exception: {}".format(ex))
        start()
    finally:
        pass
