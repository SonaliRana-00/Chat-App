from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecret'
socketio = SocketIO(app)

@app.route('/')
def chat():
    return render_template('./chat_app.html')

@socketio.on('my event')
def handle_event(json):
    print('Message Received:' + str(json))
    socketio.emit('my response' , json)


if __name__ == '__main__':
    socketio.run(app, debug = True)
