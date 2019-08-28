from flask import Flask, request, abort
from flask_socketio import SocketIO
import json
from pytz import timezone
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/device', methods=['POST'])
def foo():
    if not request.json:
        abort(400)
    result = request.json

    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    KST = datetime.now(timezone('Asia/Seoul'))
    result["time"] = KST.strftime(fmt)
    print(result)

    socketio.emit('my response', result, callback=None)
    return json.dumps(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)