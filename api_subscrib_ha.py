import paho.mqtt.client as mqtt
import pymongo, json, pprint
from logstash_input import log_input

MQTT_SERVER = "221.149.196.100"
MQTT_PATH = "hasensor/#"
USER_NAME = "jiguem"
PWD = "jigeum!"
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))
    data = json.loads(msg.payload)
    topic = str(msg.topic).replace("hasensor/","").split("/")

    data["device_type"] = topic[0]
    data["topic"] = "/".join(topic[1:])

    mongoUpdate("ha_sensors", data)
    # more callbacks, etc

def mongoUpdate(collectionName, data):
    if data == [] or data == None:
        return
    # conn = pymongo.MongoClient('221.149.196.100', 27017,username='jiguem',password='jigeum!')
    # db = conn.get_database('jiot_log')
    conn = pymongo.MongoClient('mongodb://jiguem:jigeum!@221.149.196.100:27017/default_db?authSource=jiot_log')
    db = conn.get_database('jiot_log')
    collection = db.get_collection(collectionName)

    #logstash
    log_input(data)

    collection.insert(data)
    print("insert ok!")

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