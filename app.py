from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(msg):
    # Emite a mensagem original do usuário para todos os clientes
    emit('message', f'Usuário: {msg}', broadcast=True)

    # Emite a resposta do servidor
    emit('message', 'Servidor: Oi!', broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)