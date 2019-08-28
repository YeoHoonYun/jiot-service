import json

from requests import post

if __name__ == '__main__':
    url = "http://183.98.182.142:5002/device1"
    headers = {
        'Content-Type': 'application/json',
        'Accept' : 'application/json'
    }
    data = {
		"deviceData": '{"entity_id":"light.hue_color_lamp_3","rgb_color": [247,171,81]}',
		"deviceDomain": "light",
		"deviceId": "light.hue_color_lamp_3",
		"deviceService": "turn_on",
		"time": "07:00:30",
		"dcmPk": 94,
		"usrPk": "3:618DC67618FDE401ED0D74138EB3A59D",
		"usrCode": 3,
		"statCode": 1,
		"outCond": 1,
		"tit": "테스트 메시지입니다.",
		"message": '{"type":"01","content":"테스트 내용입니다."}',
		"interv": 32,
		"inDt": [2019, 5, 10, 15, 1, 58],
		"msgtyp": 103002,
		"isgroupmsg": False,
		"isshowmsg": True,
		"dt": "2019-05-31 13:36:30 KST+0900"
	}

    res = post(url
               , headers=headers
               , data=json.dumps(data)
               ).text
    print(res)