from flask import Flask, request, abort
from flask_socketio import SocketIO
from requests import post
import json, time
from pytz import timezone
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/device', methods=['POST'])
def foo():
    if not request.json:
        abort(400)
    massege = request.json
    url = "http://jiot.jiguem.com:8081/api/devicecommand/publishcommand"
    headers = {
        'Content-Type': 'application/json'
    }
    res = json.loads(post(url
               , headers=headers
               , data=json.dumps(massege)
               ).text)
    str = json.loads(res["message"])["clientId"]
    url = "http://jiot.jiguem.com:8081/api/devicecommand/getdevicecommandresult/%s" % (str)
    # url ="http://221.149.196.100:8081/api/devicecommand/getdevicecommandresult/paho3377258905942428"
    # print(url)
    time.sleep(1)
    # print(url)
    result = post(url
               , headers=headers
               , data=json.dumps({})
               )

    result = json.loads(result.text)
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    KST = datetime.now(timezone('Asia/Seoul'))
    result["time"] = KST.strftime(fmt)
    # print(result)

    socketio.emit('my response', result, callback=None)
    return json.dumps(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)