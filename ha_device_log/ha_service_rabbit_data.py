#!/usr/bin/env python
import pika
import pymongo, json, pprint
from requests import post

credentials = pika.PlainCredentials('jiguem', 'jigeum!')
parameters = pika.ConnectionParameters(
    host='jiot.jiguem.com',
    port=5672,
    credentials=credentials,
    heartbeat=60
    )

url = "http://demo.jiguem.com:5002/device1"
headers = {
    'Content-Type': 'application/json'
}
test = True

def callback(ch, method, properties, body):
    pprint.pprint(str(body.decode("utf-8")))
    try:
        # mongodb
        mongoUpdate(json.loads(body.decode("utf-8")), 'ha_service_log')
    except:
        mongoUpdate(json.loads(body.decode("utf-8")), 'ha_service_log')

def mongoUpdate(data, connection):
    conn = pymongo.MongoClient('mongodb://jiguem:jigeum!@jiot.jiguem.com:27017/default_db?authSource=jiot_log')
    db = conn.get_database('jiot_log')
    collection = db.get_collection(connection)
    collection.insert(data)

def main():
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='haservice')
    channel.basic_consume(on_message_callback = callback,
                        queue='haservice', auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()