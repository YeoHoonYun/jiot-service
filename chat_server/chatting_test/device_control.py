from requests import post
import json

def su_mon(body):
    data = {
      "domain": "light",
      "httpMethod": "POST",
      "messageType": "COMMAND",
      "service": "turn_on",
      "serviceData": {
        "entity_id": "light.gateway_light_7c49ebb0a7f0"
      },
        "ulPk":10000
    }
    return data

def su_mon_off(body):
    data = {
      "domain": "light",
      "httpMethod": "POST",
      "messageType": "COMMAND",
      "service": "turn_off",
      "serviceData": {
        "entity_id": "light.gateway_light_7c49ebb0a7f0"
      },
        "ulPk":10000
    }
    return data

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