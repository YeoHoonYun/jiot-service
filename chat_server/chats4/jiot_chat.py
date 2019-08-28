from flask import Flask, request, abort, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin
from pytz import timezone
from datetime import datetime
from chat_test import *
import json, pymongo, pprint


# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
# socketio = SocketIO(app)
#
# @app.route('/device1', methods=['POST', 'OPTIONS'])
# @cross_origin()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'

cors = CORS(app, resources={r"*": {"origins": "*"}})
socketio = SocketIO(app)

@app.route('/device1', methods=['POST',"GET"])
@cross_origin(app)
def foo():
    if not request.json:
        abort(400)

    result = json.loads(request.data)
    # print(type(result))
    # pprint.pprint(result)
    try:
        # mongodb
        mongoUpdate(json.loads(json.dumps(result)))
    except:
        mongoUpdate(json.loads(json.dumps(result)))

    if type(result["usrPk"]) != list:
        result["usrPk"] = [result["usrPk"]]

    result["dt"] = get_kst()
    # pprint.pprint(result)

    if result.get("msgtyp") == 103005 or result.get("msgTyp") == 103005:
        massage = json.loads(result["message"])
        result["message"] = json.dumps({
            "ID" : massage["ID"],
            "msg" : word_anal(massage["msg"], result)
        })
        result["tit"] = "완료 메시지"
        # print("anal")
        # print(json.loads(result["message"])["msg"])

    for uid in result.get("uidList"):
        print(uid)
        if(result.get('isShowMsg') == False or result.get("msgTyp") == 103001):
            pass
        pprint.pprint(result)
        socketio.emit(str(uid), result, callback=messageReceived)

    return json.dumps(result)

def get_kst():
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    KST = datetime.now(timezone('Asia/Seoul'))
    return KST.strftime(fmt)

def mongoUpdate(data):
    conn = pymongo.MongoClient('mongodb://jiguem:jigeum!@183.98.179.130:27017/default_db?authSource=jiot_log')
    db = conn.get_database('jiot_log')
    collection = db.get_collection('send_messages')
    collection.insert(data)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)