#!/usr/bin/env python
import pika
import datetime
import time
import random
import json

credentials = pika.PlainCredentials('jiguem', 'jigeum!')
parameters = pika.ConnectionParameters(
    host='221.149.196.100',
    port=5672,
    virtual_host='jiot',
    credentials=credentials,
    heartbeat=60)

def send(payload):
    try:
        # connection = pika.BlockingConnection(pika.ConnectionParameters(host='221.149.196.100'))
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        jsonStr = json.dumps(payload)
        channel.queue_declare(queue='jiot')
        channel.basic_publish(exchange='',
                            routing_key='jiot',
                            body=jsonStr)
        print(" [x] Sent message")
        # connection.close()

    except Exception as ex:
        print("Error: %s" % ex)
    finally:
        connection.close()

if __name__ == "__main__":

    for  i in range(0, 100000000):
        try:
            t1 = random.randint(1, 90) * 0.01
            dt = datetime.datetime.now()
            print ("[{0}] rabbitmq message sending: {1}".format(datetime.datetime.now(), i))
            payload = {"no": i, "dt": dt.strftime("%Y-%m-%d %H:%M:%S"), "message": "hello jiot!", "data": {"x": i, "y": t1}}
            send(payload)
            time.sleep(t1)

        except Exception as ex:
            print ("Exception: %s" % ex)
            time.sleep(5)