#!/usr/bin/env python
import pika
import pymongo, json

credentials = pika.PlainCredentials('jiguem', 'jigeum!')
parameters = pika.ConnectionParameters(
    host='221.149.196.100',
    port=5672,
    # virtual_host='/',
    virtual_host='jiot',
    credentials=credentials,
    heartbeat=60
    )

def callback(ch, method, properties, body):
    print(body)
    mongoUpdate(json.loads(body))
    # print(" [x] Received %r" % body)

def mongoUpdate(data):
    # conn = pymongo.MongoClient('221.149.196.100', 27017)
    conn = pymongo.MongoClient('mongodb://jiguem:jigeum!@221.149.196.100:27017/default_db?authSource=jiot_log')
    db = conn.get_database('jiot_log')
    collection = db.get_collection('hue_light2')
    collection.insert(data)
    # print("insert ok!")

def main():
    try:
        connection = pika.BlockingConnection(parameters)
        # connection = pika.BlockingConnection(pika.ConnectionParameters(host='221.149.196.100'))
        channel = connection.channel()
        channel.queue_declare(queue='jiot')
        channel.basic_consume(on_message_callback = callback,
                            queue='jiot')
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    except Exception as ex:
        print("Exception: {}".format(ex))
    finally:
        pass

if __name__ == "__main__":
    main()