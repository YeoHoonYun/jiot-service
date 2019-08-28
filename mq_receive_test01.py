#!/usr/bin/env python
import pika
import datetime
import time
import random

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
    print ("[{0}] rabbitmq message received: \r{1}\r".format(datetime.datetime.now(), body))
    # print(" [x] Received %r" % body)

    # TODO: data handling
    t1 = random.randint(1, 80) * 0.01
    time.sleep(t1)

def main():
    try:
        connection = pika.BlockingConnection(parameters)
        # connection = pika.BlockingConnection(pika.ConnectionParameters(host='221.149.196.100'))
        channel = connection.channel()
        channel.queue_declare(queue='jiot')
        channel.basic_consume(callback,
                            queue='jiot',
                            #no_ack=True
                            )
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    except Exception as ex:
        print("Exception: {}".format(ex))
    finally:
        pass

if __name__ == "__main__":
    main()