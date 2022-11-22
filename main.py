from flask import Flask
from Controller.user_ctrl import create_user

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ''


@app.route("/user/<name>")
def hello(name):
    id_user = create_user(name)
    return f'<p>{id_user}</p>'


if __name__ == '__main__':
    app.run()


