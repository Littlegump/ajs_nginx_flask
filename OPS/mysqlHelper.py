# _*_ coding: utf-8 _*_

import pymysql

class getData(object):
    def __init__(self, sql):
        self.sql = sql
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd = 'redhat',
            db='phones'
        )
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def execsql(self):
        rec = self.cur.execute(self.sql)
        data = self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return data

sql = 'select * from phonelist'
my = getData(sql)
data = my.execsql()