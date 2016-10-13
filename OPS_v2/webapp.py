# _*_ coding: utf-8 _*_

import json

from flask import Flask, render_template

from config.conf import run_flask_dict
from model.phonelist import Opr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test/phonelist',methods=['GET'])
def v_user():
    handle = Opr()
    data = json.dumps(handle.getAll())
    return data

@app.route('/adduser')
def adduser():
    return '123'

if __name__ == "__main__":
    app.run(**run_flask_dict)