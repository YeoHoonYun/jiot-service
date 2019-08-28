#!/usr/bin/env python
import pika
import pymongo, json, pprint
import chat_test
from logstash_input import log_input

from requests import post

credentials = pika.PlainCredentials('jiguem', 'jigeum!')
parameters = pika.ConnectionParameters(
    host='jiot.jiguem.com',
    port=5672,
    credentials=credentials,
    heartbeat=60
    )

# url = "http://demo.jiguem.com:5002/device1"
# headers = {'Content-Type': 'application/json'}
test = True

def callback(ch, method, properties, body):
    pprint.pprint(str(body.decode("utf-8")))
    check_list = ["binary_sensor.door_window_sensor", "binary_sensor.switch"]

    if(json.loads(body.decode("utf-8"))["test"] == "yun"):
        try:
            chat_post(json.loads(body.decode("utf-8")), check_list, url="http://demo.jiguem.com:5003/device1",
                      headers={'Content-Type': 'application/json'})
        except:
            chat_post(json.loads(body.decode("utf-8")), check_list, url="http://demo.jiguem.com:5003/device1",
                      headers={'Content-Type': 'application/json'})

    elif (test and json.loads(body.decode("utf-8"))["ulPk"] < 10000):
        try:
            chat_post(json.loads(body.decode("utf-8")), check_list, url = "http://demo.jiguem.com:5002/device1", headers = {'Content-Type': 'application/json'})
        except:
            chat_post(json.loads(body.decode("utf-8")), check_list, url = "http://demo.jiguem.com:5002/device1", headers = {'Content-Type': 'application/json'})

    try:
        print(json.loads(body.decode("utf-8")))
        # mongodb
        mongoUpdate(json.loads(body.decode("utf-8")), 'ha_sensors_state')
    except:
        mongoUpdate(json.loads(body.decode("utf-8")), 'ha_sensors_state')

    try:
        # logstash
        log_input(json.loads(body.decode("utf-8")))
    except:
        log_input(json.loads(body.decode("utf-8")))


def chat_post(body, check_list, url, headers):
    for check in check_list:
        if check in body["entity_id"]:
            print(body)
            message = chat_test.word_dict(body)
            res = post(url
                       , headers=headers
                       , data=json.dumps(message)
                       ).text
            print(res)

def mongoUpdate(data,connection):
    conn = pymongo.MongoClient('mongodb://jiguem:jigeum!@jiot.jiguem.com:27017/default_db?authSource=jiot_log')
    db = conn.get_database('jiot_log')
    collection = db.get_collection(connection)
    collection.insert(data)

def main():
    # try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='hasensor')
    channel.basic_consume(on_message_callback = callback,
                        queue='hasensor', auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()