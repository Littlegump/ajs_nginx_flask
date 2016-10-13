# _*_ coding: utf-8 _*_

import pymysql


conn_mysql_dict = dict(
    host='localhost',
    user = 'root',
    password = 'redhat',
    db = 'phones',
    cursorclass = pymysql.cursors.DictCursor
)


run_flask_dict = dict(
    host='0.0.0.0',
    port=1234,
    debug=True
)