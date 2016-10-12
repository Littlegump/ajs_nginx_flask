# _*_ coding: utf-8 _*_

from flask import Flask, render_template, jsonify
import mysqlHelper
import json

app = Flask(__name__)

host="0.0.0.0"
port=1234


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test/phonelist',methods=['GET'])
def v_user():
    sql = 'select * from phonelist'
    conn = mysqlHelper.getData(sql)
    data = json.dumps(conn.execsql())
    print data
    return data

@app.route('/adduser')
def adduser():
    return '123'

if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)