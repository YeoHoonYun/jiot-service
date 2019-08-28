from requests import post, get
import json, time

class HomeassistantService:
    def __init__(self):
        self.url = 'http://172.30.1.38:8123/api/services'
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0Njg4ZjcyNmI1OTM0ZWMyOTI5Nzg3OTYxOTkxYTliYSIsImlhdCI6MTU1MzA0NDA0MywiZXhwIjoxODY4NDA0MDQzfQ.L8w6WlZOjqpLG5ezIkkEPM_EQXayPBpgQHk6fJSv5aY'
        }
        self.error_list = ['404: Not Found']

    def curtain_open(self):
        print('문열림')
        #문열림
        url = 'http://172.30.1.38:8123/api/services/python_script/curtain_close'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0Njg4ZjcyNmI1OTM0ZWMyOTI5Nzg3OTYxOTkxYTliYSIsImlhdCI6MTU1MzA0NDA0MywiZXhwIjoxODY4NDA0MDQzfQ.L8w6WlZOjqpLG5ezIkkEPM_EQXayPBpgQHk6fJSv5aY'
        }
        data = '''{
          "entity_id": "cover.curtain_158d0002830a0b"
        }'''
        print(post(url, headers=headers, data=data).text)

    def curtain_close(self):
        print('문닫힘')
        #문닫힘
        url = 'http://172.30.1.38:8123/api/services/python_script/curtain_open'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0Njg4ZjcyNmI1OTM0ZWMyOTI5Nzg3OTYxOTkxYTliYSIsImlhdCI6MTU1MzA0NDA0MywiZXhwIjoxODY4NDA0MDQzfQ.L8w6WlZOjqpLG5ezIkkEPM_EQXayPBpgQHk6fJSv5aY'
        }
        data = '''{
          "entity_id": "cover.curtain_158d0002830a0b"
        }'''
        print(post(url, headers=headers, data=data).text)

    def light_on(self, domain, service, entity, client):
        print('불켜짐')
        try:
            # 불켜짐
            url = self.url + '/' + domain + '/' + service
            data = '''{
                      "entity_id": "%s"
                    }''' % (entity['entity_id'])

            post_result = post(url, headers=self.headers, data=data).text
            for error in self.error_list:
                if error in post_result:
                    return {'success': False, 'clientId': client, "error" : error}
            return {'success': True, 'clientId' : client, 'post_result' : post_result}

        except:
            return {'success': False, 'clientId' : client, "error" : 'System Error'}

    def light_off(self, domain, service, entity, client):
        print('불꺼짐')
        try:
            # 불꺼짐
            url = self.url + '/' + domain + '/' + service
            data = '''{
                      "entity_id": "%s"
                    }''' % (entity['entity_id'])
            post_result = post(url, headers=self.headers, data=data).text
            for error in self.error_list:
                if error in post_result:
                    return {'success': False, 'clientId': client, "error" : error}
            return {'success': True, 'clientId' : client, 'post_result' : post_result}

        except:
            return {'success': False, 'clientId' : client, "error" : 'System Error'}

if __name__ == "__main__":
    homeassistantService = HomeassistantService()
    # HomeassistantService.light_on()
    # time.sleep(5)
    # HomeassistantService.light_off()

    # text1 = '{"domain":"light","service":"turn_on","serviceData":{"entity_id":"light.hue_color_lamp_1"},"clientId":"paho84484433185300"}'
    # text2 = '{"domain":"light","service":"turn_off","serviceData":{"entity_id":"light.hue_color_lamp_1"},"clientId":"paho84484433185300"}'

    # data1 = json.loads(text1)
    # data2 = json.loads(text2)

    # print(homeassistantService.light_on(data1['domain'], data1['service'], data1['serviceData'], data1['clientId']))
    # time.sleep(5)
    # print(homeassistantService.light_off(data2['domain'], data2['service'], data2['serviceData'], data2['clientId']))

    # # 에러(404)
    # time.sleep(5)
    # print(homeassistantService.light_on('', data1['service'], data1['serviceData'], data1['clientId']))

    homeassistantService.curtain_close()
    # homeassistantService.curtain_open()