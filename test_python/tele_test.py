from requests import post
import json
from test_python import ChatBotModel
from test_python.ha_rest import HomeassistantService

def proc_rolling(bot, update):
    chii.sendMessage('데구르르..')
    sound = firecracker()
    chii.sendMessage(sound)
    chii.sendMessage('르르..')

def proc_stop(bot, update):
    chii.sendMessage('치이 봇이 잠듭니다.')
    # chii.stop()

def bot_curtain_open(bot, update):
    chii.sendMessage('Jiguem 커튼을 엽니다.')
    url = 'http://183.98.179.130:8081/api/devicecommand/publishcommand'
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
              "domain": "cover",
              "httpMethod": "POST",
              "messageType": "COMMAND",
              "service": "close_cover",
              "serviceData": {
                "entity_id": "cover.curtain_158d0002830a0b"
              },
              "usrPk": 1
            }
    result = post(url
               , headers=headers
               , data=json.dumps(data)
               )

def bot_curtain_close(bot, update):
    chii.sendMessage('Jiguem 커튼을 닫습니다.')
    url = 'http://183.98.179.130:8081/api/devicecommand/publishcommand'
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
          "domain": "cover",
          "httpMethod": "POST",
          "messageType": "COMMAND",
          "service": "open_cover",
          "serviceData": {
            "entity_id": "cover.curtain_158d0002830a0b"
          },
          "usrPk": 1
        }
    result = post(url
                  , headers=headers
                  , data=json.dumps(data)
                  )

def firecracker():
    return '팡팡!'


ha = HomeassistantService()

chii = ChatBotModel.BotChii()
chii.add_handler('rolling', proc_rolling)
chii.add_handler('stop', proc_stop)
chii.add_handler('jiguem_open', bot_curtain_open)
chii.add_handler('jiguem_close', bot_curtain_close)
chii.start()