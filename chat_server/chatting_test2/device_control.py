from requests import post
import json
data = {
    "usrPk" : 50,
    "ulPk" : 10001,
    "uidList" : ["52622fb9-6770-468f-9e02-2462deccc0f6"],
    "msgTyp" : 103001,
    "isShowMsg" : True,
    "isGroupMsg" : False
}
device_list = {
    "group.all_covers": "모든_커튼",
    "group.all_fans": "모든_공기청정기",
    "group.all_lights": "모든_불",

    "light.light_yeelight_ceiling": "천정등",
    "light.light_yeelight_bulb02": "화장실 조명",
    "cover.blind": "블라인드",
    "light.light_yeelight_lamp01": "침실등",
    "light.light_yeelight_table": "책상등",
    "light.light_yeelight_lamp02": "무드등",
    "cover.curtain_158d0002edad4d": "커튼",
    "light.light_yeelight_bulb03": "부엌 조명",
    "vacuum.xiaomi_vacuum_cleaner": "로봇청소기",
    "fan.xiaomi_miio_device": "공기청정기1",
    "fan.xiaomi_miio_device_2": "공기청정기2"
}

def chat_message(message,id="b10",TMX="", TMN="" ,body=""):
    data = {
        "usrPk": 50,
        "ulPk": 10001,
        "tit": "알림",
        "TMX": TMX,
        "TMN": TMN,
        "ID": id,
        "message": message,
        "msgTyp": 103002,
        "uidList": ["52622fb9-6770-468f-9e02-2462deccc0f6"],
        "isShowMsg": True,
        "isGroupMsg": False,
    }
    return json.dumps(data)

def time_sleep(time, body=""):
    data = {
      "timeSleep" : int(time)
    }
    return json.dumps(data)

def light_on(device, body=""):
    data.update({
      "tit" : "알림",
      "message" : json.dumps({
                    "ID" : "b10",
                    "msg" : "%s이(가) 켰습니다." % device_list.get(device)
                }),
      "domain": "light",
      "httpMethod": "POST",
      "messageType": "COMMAND",
      "service": "turn_on",
      "serviceData": {
        "entity_id": device,
        "rgb_color": [255, 255, 255]
      }
    })
    return json.dumps(data)

def light_off(device, body=""):
    data.update({
      "tit": "알림",
        "message" : json.dumps({
                "ID" : "b10",
                "msg" : "%s이(가) 껐습니다." % device_list.get(device)
            }),
      "domain": "light",
      "httpMethod": "POST",
      "messageType": "COMMAND",
      "service": "turn_off",
      "serviceData": {
        "entity_id": device
      }
    })
    return json.dumps(data)

def light_brightness(device, brightness="",color="" ,body=""):
    data.update({
      "tit": "알림",
            "message" : json.dumps({
                    "ID" : "b10",
                    "msg" : "%s의 밝기를 조절하였습니다." % device_list.get(device)
                }),
      "domain": "light",
      "httpMethod": "POST",
      "messageType": "COMMAND",
      "service": "turn_on",
      "serviceData": {
        "entity_id": device,
        "brightness": brightness,
        "rgb_color" : color
      }
    })
    return json.dumps(data)

def cover_on(device, body=""):
    data.update({
      "tit": "알림",
            "message" : json.dumps({
                    "ID" : "b10",
                    "msg" : "%s이(가) 열었습니다." % device_list.get(device)
                }),
      "domain": "cover",
      "httpMethod": "POST",
      "messageType": "COMMAND",
      "service": "set_cover_position",
      "serviceData": {
        "entity_id": device,
        "position": 100
      }
    })
    return json.dumps(data)

def cover_off(device, body=""):
    data.update({
      "tit": "알림",
            "message" : json.dumps({
                    "ID" : "b10",
                    "msg" : "%s을(를) 닫았습니다." % device_list.get(device)
                }),
      "domain": "cover",
      "httpMethod": "POST",
      "messageType": "COMMAND",
      "service": "set_cover_position",
      "serviceData": {
        "entity_id": device,
        "position": 0
      }
    })
    return json.dumps(data)

def cover_position(device, body=""):
    data.update({
      "tit": "알림",
            "message" : json.dumps({
                    "ID" : "b10",
                    "msg" : "%s의 길이를 조절하였습니다." % device_list.get(device)
                }),
      "domain": "cover",
      "httpMethod": "POST",
      "messageType": "COMMAND",
      "service": "set_cover_position",
      "serviceData": {
        "entity_id": device,
        "position": 50
      }
    })
    return json.dumps(data)

def robot_start(device, body=""):
    data.update({
      "tit": "알림",
            "message" : json.dumps({
                    "ID" : "b10",
                    "msg" : "%s이(가) 청소를 시작합니다." % device_list.get(device)
                }),
      "domain": "vacuum",
      "httpMethod": "POST",
      "messageType": "COMMAND",
      "service": "start",
      "serviceData": {
        "entity_id": device
      }
    })
    return json.dumps(data)

def robot_stop(device, body=""):
    data.update({
      "tit": "알림",
            "message" : json.dumps({
                    "ID" : "b10",
                    "msg" : "%s이(가) 청소를 종료합니다." % device_list.get(device)
                }),
      "domain": "vacuum",
      "httpMethod": "POST",
      "messageType": "COMMAND",
      "service": "stop",
      "serviceData": {
        "entity_id": device
      }
    })
    return json.dumps(data)
def robot_back(device, body=""):
    data.update({
      "tit": "알림",
            "message" : json.dumps({
                    "ID" : "b10",
                    "msg" :"%s이(가) 되돌아갑니다." % device_list.get(device)
                }),
      "domain": "vacuum",
      "httpMethod": "POST",
      "messageType": "COMMAND",
      "service": "return_to_base",
      "serviceData": {
        "entity_id": device
      }
    })
    return json.dumps(data)

def fan_start(device, body=""):
    data.update({
      "tit": "알림",
            "message" : json.dumps({
                    "ID" : "b10",
                    "msg" : "%s을(를) 켰습니다." % device_list.get(device)
                }),
      "domain": "fan",
      "httpMethod": "POST",
      "messageType": "COMMAND",
      "service": "turn_on",
      "serviceData": {
        "entity_id": device
      }
    })
    return json.dumps(data)

def fan_stop(device, body=""):
    data.update({
      "tit": "알림",
            "message" : json.dumps({
                    "ID" : "b10",
                    "msg" : "%s을(를) 껐습니다." % device_list.get(device)
                }),
      "domain": "fan",
      "httpMethod": "POST",
      "messageType": "COMMAND",
      "service": "turn_off",
      "serviceData": {
        "entity_id": device
      }
    })
    return json.dumps(data)

# def hue1_turn_on():
#     data = {
#       "domain": "light",
#       "httpMethod": "POST",
#       "messageType": "COMMAND",
#       "service": "turn_on",
#       "serviceData": {
#         "entity_id": "light.hue_color_lamp_1"
#       }
#     }
#     post(url, headers=headers, data=json.dumps(data))
#     return data
#
# def hue1_turn_off():
#     data = {
#       "domain": "light",
#       "httpMethod": "POST",
#       "messageType": "COMMAND",
#       "service": "turn_off",
#       "serviceData": {
#         "entity_id": "light.hue_color_lamp_1"
#       }
#     }
#     return data
#
# def hue2_turn_on():
#     data = {
#         "domain": "light",
#         "httpMethod": "POST",
#         "messageType": "COMMAND",
#         "service": "turn_on",
#         "serviceData": {
#             "entity_id": "light.hue_color_lamp_2"
#         }
#     }
#     return data
#
# def hue2_turn_off():
#     data = {
#         "domain": "light",
#         "httpMethod": "POST",
#         "messageType": "COMMAND",
#         "service": "turn_off",
#         "serviceData": {
#             "entity_id": "light.hue_color_lamp_2"
#         }
#     }
#     return data
#
# def hue3_turn_on():
#     data = {
#         "domain": "light",
#         "httpMethod": "POST",
#         "messageType": "COMMAND",
#         "service": "turn_on",
#         "serviceData": {
#             "entity_id": "light.hue_color_lamp_3"
#         }
#     }
#     return data
#
# def hue3_turn_off():
#     data = {
#         "domain": "light",
#         "httpMethod": "POST",
#         "messageType": "COMMAND",
#         "service": "turn_off",
#         "serviceData": {
#             "entity_id": "light.hue_color_lamp_3"
#         }
#     }
#     return data
#
# def curtain_open():
#     data = {
#         "domain": "cover",
#         "httpMethod": "POST",
#         "messageType": "COMMAND",
#         "service": "close_cover",
#         "serviceData": {
#             "entity_id": "cover.curtain_158d0002830a0b"
#         }
#     }
#     return data
#
# def curtain_close():
#     data = {
#         "domain": "cover",
#         "httpMethod": "POST",
#         "messageType": "COMMAND",
#         "service": "open_cover",
#         "serviceData": {
#             "entity_id": "cover.curtain_158d0002830a0b"
#         }
#     }
#     return data
#
# def all_light_on():
#     data = {
#         "domain": "light",
#         "httpMethod": "POST",
#         "messageType": "COMMAND",
#         "service": "turn_on",
#         "serviceData": {
#             "entity_id": "group.all_lights"
#         }
#     }
#     return data
#
# def all_light_off():
#     data = {
#         "domain": "light",
#         "httpMethod": "POST",
#         "messageType": "COMMAND",
#         "service": "turn_off",
#         "serviceData": {
#             "entity_id": "group.all_lights"
#         }
#     }
#     return data

def null():
    pass