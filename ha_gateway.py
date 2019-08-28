import paho.mqtt.client as mqtt
from requests import get, post
import json, pprint, datetime, time

class hasensor:
    def __init__(self):
        self.utctime = datetime.datetime.utcnow()
        self.nowtime = str(datetime.datetime.utcnow()).replace(" ", "T")[:-3] + "Z"
        self.now_minus_time = str(datetime.datetime.utcnow() - datetime.timedelta(days=1)).replace(" ", "T")[:-3] + "Z"

    def getAccessToken(self):
        url = 'http://172.30.1.39:8123/auth/token'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'client_id': 'http://172.30.1.39:8123/',
            'grant_type': 'refresh_token',
            'refresh_token': 'd70971081e33eaac700dd1e596d69dc4351fc0c5248bc88b794216a8cb5bed0aeba2b50d9ea5baafac239de886093ed0e422d29e6d6e29f2ead88dac03a7394d'
        }
        return json.loads(post(url, headers=headers, data=data).text)['access_token']

    def getNowTime(self):
        return str(self.utctime).replace(" ", "T")[:-3] + "Z", str(self.utctime - datetime.timedelta(days=1)).replace(
            " ", "T")[:-3] + "Z"

    def getHaData(self, token, now_minus_time, now_time):
        # url = 'http://172.30.1.39:8123/api/history/period/2019-03-12T15:00:00.000Z?end_time=2019-03-13T15:00:00.000Z'
        url = 'http://172.30.1.39:8123/api/history/period/%s?end_time=%s' % (now_minus_time, now_time)
        headers = {
            'Authorization': 'Bearer ' + token,
            'content-type': 'application/json',
        }
        return json.loads(get(url, headers=headers).text)


def pubData(mqttc, topic, data, ho, dong):
    print(data['entity_id'])
    data['dt'] = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    pprint.pprint(data)
    print("hasensor/" + topic + "/" + ho + "/"+dong)
    mqttc.publish("hasensor/" + topic + "/" + ho + "/"+dong, json.dumps(data))


if __name__ == "__main__":
    # 기본 필드 설정
    hasensor = hasensor()
    client_name = "python_pub"
    client_ip = "221.149.196.100"
    client_port = 1883
    ho = "406"
    dong = "503"
    entity_list = [
      'binary_sensor.door_window_sensor'
    , 'binary_sensor.motion_sensor'
    # , 'cover.curtain'
    # , 'light.gateway_light'
    # , 'light.geosil'
    # , 'light.hue_color_lamp'
    # , 'sensor.fibaro_illuminance'
    # , 'sensor.fibaro_motion'
    # , 'sensor.fibaro_tamper'
    # , 'sensor.fibaro_temperature'
    ]

    while (True):
        # access_token 가져오기
        token = hasensor.getAccessToken()
        print(token)

        # sensor로그 최근 데이터 가져오기
        now_time, now_minus_time = hasensor.getNowTime()

        json_data = hasensor.getHaData(token, now_minus_time, now_time)
        mqttc = mqtt.Client(client_name)
        mqttc.connect(client_ip, client_port)

        mqttc.loop(5)

        # 필요한 데이터 전송
        for jdata in json_data:
            print(jdata)
            for i in jdata:
                for entity in entity_list:
                    if (entity in i['entity_id']):
                        print(i)
            # last_info = jdata[len(jdata) - 1]
            # for entity in entity_list:
            #     if (entity in last_info['entity_id']):
            #         print(last_info)
                    # pubData(mqttc, entity, last_info, ho, dong)

        time.sleep(5)