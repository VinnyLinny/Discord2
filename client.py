from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)
@app.route('/chat')
def chat():
    return render_template('chat.html')
@socketio.on('message')
def handle_message(msg):
    # Extract the name and message from the received message
    name, message = msg.split(separator_token)
    # Process the message as needed
    # ...
    # Emit the modified message to all connected clients
    emit('message', f"{client_color}[{date_now}] {name}: {message}{Fore.RESET}", broadcast=True)
if __name__ == '__main__':
    socketio.run(app)
