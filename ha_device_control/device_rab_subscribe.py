#!/usr/bin/env python
import pika, json
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

def callback(ch, method, properties, body):
    data = json.loads(body)

    is_show = data["isShowMsg"]
    if is_show == None:
        is_show = True

    # print("--------------------------------------")
    # print("1")
    # print(data)
    # print("2")
    # print(data["isShowMsg"] == True)
    # print("3")
    # print(data.get("uidList"))
    # print("4")
    # print(type(data.get("uidList")))
    # print("5")
    # # print(data.get("uidList")[0])
    # print(data.get("uidList") == "None")
    # print("6")
    # print(data.get("uidList") == None)
    # print("--------------------------------------")

    # try:
    if(data.get("uidList") != None):
        url = 'https://jiot.iotjiguem.com/device1'
        headers = {
            'Content-Type': 'application/json'
        }
        try:
            post(url, headers=headers, data=json.dumps(data))
        except:
            pass
    else:
        url = "http://demo.jiguem.com:5002/device1"
        headers = {
            'Content-Type': 'application/json'
        }
        if is_show:
            res = post(url
                       , headers=headers
                       , data=json.dumps(data)
                       )
    # except:
    #     pass

        # print(res.text)
        # print(res.status_code)
        # print(str(body.decode("utf-8")))

def main():
    # try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='hasensor_message')
    channel.basic_consume(on_message_callback = callback,
                        queue='hasensor_message', auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()