import paho.mqtt.client as mqtt
import json, pprint
from rab_publish import rabbit_send
from pytz import timezone
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe(MQTT_PATH)

def get_kst():
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    KST = datetime.now(timezone('Asia/Seoul'))
    return KST.strftime(fmt)

def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))
    data = json.loads(msg.payload)
    topic = str(msg.topic).replace("hasensor/","").split("/")

    data["device_type"] = topic[0]
    data["topic"] = "/".join(topic[1:])
    data["dt"] = get_kst()

    try:
        # rabbitMQ
        pprint.pprint(data)
        rabbit_send(data, queue='hasensor')
    except:
        rabbit_send(data, queue='hasensor')

if __name__ == "__main__":
    MQTT_SERVER = "jiot.jiguem.com"
    MQTT_PATH = "hasensor/#"
    USER_NAME = "jiguem"
    PWD = "jigeum!"

    client = mqtt.Client()
    client.username_pw_set(USER_NAME, PWD)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_SERVER, 1883, 60)

    client.loop_forever()