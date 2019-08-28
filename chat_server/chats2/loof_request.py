from requests import post
import json, time, random

url = "http://127.0.0.1:5001/device"
headers = {
    'Content-Type': 'application/json'
}
commands = [
    ["hue_on",["light", "turn_on", "light.hue_color_lamp_1"]],
    ["hue_off",["light", "turn_off", "light.hue_color_lamp_1"]],
    ["gateway_on",["light", "turn_on", "light.gateway_light_7c49eb1b27ef"]],
    ["gateway_off",["light", "turn_off", "light.gateway_light_7c49eb1b27ef"]],
    ["curtain_open",["cover", "close_cover", "cover.curtain_158d0002830a0b"]],
    ["curtain_close",["cover", "open_cover", "cover.curtain_158d0002830a0b"]]
]
# data = {
#           "domain": "light",
#           "httpMethod": "POST",
#           "messageType": "COMMAND",
#           "service": "turn_off",
#           "serviceData": {
#             "entity_id": "light.hue_color_lamp_1"
#           }
#         }
data = {"serviceData": {}}
while True:
    for command in commands:
        print(command[0])
        data["domain"] = command[1][0]
        data["httpMethod"] = "POST"
        data["messageType"] = "COMMAND"
        data["service"] = command[1][1]
        data["serviceData"]["entity_id"] = command[1][2]
        res = post(url
                   , headers=headers
                   , data=json.dumps(data)
                   ).text
        print(res)
        time.sleep(random.choice(range(1,10)))