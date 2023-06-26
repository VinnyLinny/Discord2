from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import io


app = Flask(__name__, static_folder='static') 
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)
# store connected clients
client_sockets = set()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@socketio.on('connect')
def handle_connect():
    client_sockets.add(request.sid)
    print(f"[+] {request.sid} connected.")

separator_token = ":"

@socketio.on('message')
def handle_message(data):
    print(f"Received message: {data['message']}")
    modified_msg = data['message'].replace(separator_token, ": ")
    for client_socket in client_sockets:
        emit('message', {'name': data['name'], 'message': modified_msg}, room=client_socket)

@socketio.on('disconnect')
def handle_disconnect():
    client_sockets.remove(request.sid)

if __name__ == '__main__':
    socketio.run(app)