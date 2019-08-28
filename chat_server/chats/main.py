from flask import Flask, render_template
from flask_socketio import SocketIO
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    socketio.emit('my response', "test", callback=messageReceived)
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    while(True):
        socketio.emit('my response', "test", callback=messageReceived)
        time.sleep(1);
if __name__ == '__main__':
    socketio.run(app, debug=True)