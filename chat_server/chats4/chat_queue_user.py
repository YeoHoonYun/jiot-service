from flask import Flask, request, abort
from flask_socketio import SocketIO
from flask_cors import CORS
import json, random
from pytz import timezone
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
cors = CORS(app, resources={r"*": {"origins": "*"}})
socketio = SocketIO(app)

@app.route('/device1', methods=['POST'])
def foo():
    if not request.json:
        abort(400)
    result = request.json

    if type(result["usrPk"]) != list:
        result["usrPk"] = [result["usrPk"]]

    result["dt"] = get_kst()
    print(result)

    # socketio.emit(result["usrPk"], result, callback=None)
    # print(result["usrPk"].split(":")[0]+":")
    # socketio.emit(result["usrPk"].split(":")[0]+":undefined", result, callback=None)

    socketio.emit("jiguem", result, callback=None)

    return json.dumps(result)

def get_kst():
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    KST = datetime.now(timezone('Asia/Seoul'))
    return KST.strftime(fmt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)