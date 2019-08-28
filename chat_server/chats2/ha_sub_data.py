from requests import post
import paho.mqtt.client as mqtt
import json

url = "http://127.0.0.1:5002/device"
headers = {
    'Content-Type': 'application/json'
}
MQTT_SERVER = "221.149.196.100"
MQTT_PATH = "hasensor/#"
USER_NAME = "jiguem"
PWD = "jigeum!"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    topic = str(msg.topic).replace("hasensor/","").split("/")

    data["device_type"] = topic[0]
    data["topic"] = "/".join(topic[1:])

    res = post(url
               , headers=headers
               , data=json.dumps(data)
               ).text

    print(res)

if __name__ == "__main__":
    MQTT_SERVER = "221.149.196.100"
    MQTT_PATH = "hasensor/#"
    USER_NAME = "jiguem"
    PWD = "jigeum!"

    client = mqtt.Client()
    client.username_pw_set(USER_NAME, PWD)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_SERVER, 1883, 60)

    client.loop_forever()

print(res)