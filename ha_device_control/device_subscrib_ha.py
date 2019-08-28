import paho.mqtt.client as mqtt
import json, pprint
from device_rab_publish import rabbit_send

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    print(msg)
    data = json.loads(msg.payload)
    topic = str(msg.topic).replace("hasensor_message/","").split("/")


    data["usrPk"] = topic[0]
    data["topic"] = "/".join(topic[1:])

    rabbit_send(data)

if __name__ == "__main__":
    MQTT_SERVER = "jiot.jiguem.com"
    MQTT_PATH = "hasensor_message/#"
    USER_NAME = "jiguem"
    PWD = "jigeum!"

    client = mqtt.Client()
    client.username_pw_set(USER_NAME, PWD)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_SERVER, 1883, 60)

    client.loop_forever()