import json
import hashlib

from flask import Flask, Response, request
from Controller.user_ctrl import create_user

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ''

@app.route("/hash", methods=["GET","POST"])
def hash():
    #pega dado da requisicao POST e transforma texto em objeto dict.
    request_data = json.dumps(request.get_json())
    response = Response()
    response.content_type = "application/json"
    response.status_code = 200
    name = "Fabio"
    nameb = "Fernanda"
    name_hash = hashlib.sha256(name.encode("UTF-8")).hexdigest()
    nameb_hash = hashlib.sha256(nameb.encode("UTF-8")).hexdigest()
    response.data = json.dumps({"hash": [name_hash, nameb_hash, request_data]})
    return response

@app.route("/json")
def world():
    data = "{ \"name\": \"Fernanda\" }"
    dict_data = json.loads(data)
    print(dict_data)
    new_dict = dict({"name": "Fabio"})
    string_new_dict = json.dumps(new_dict)
    print(string_new_dict)
    return dict_data

@app.route("/user/<name>")
def hello(name):
    id_user = create_user(name)
    return f'<p>{id_user}</p>'


if __name__ == '__main__':
    app.run()


