import pika,json

credentials = pika.PlainCredentials('jiguem', 'jigeum!')
parameters = pika.ConnectionParameters(
    host='jiot.jiguem.com',
    port=5672,
    credentials=credentials,
    heartbeat=60)

def rabbit_send(payload, queue):
    try:
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        jsonStr = json.dumps(payload)
        channel.queue_declare(queue=queue)
        print(jsonStr)
        channel.basic_publish(exchange='',
                            routing_key=queue,
                            body=jsonStr.encode("utf-8"))
        print(" [x] Sent message")
        # connection.close()

    except Exception as ex:
        print("Error: %s" % ex)
    finally:
        connection.close()