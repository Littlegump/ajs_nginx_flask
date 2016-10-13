# _*_ coding: utf-8 _*_

import pymysql

class getData(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd = 'redhat',
            db='phones'
        )
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def execsql(self, sql, params):
        rec = self.cur.execute(sql, params)
        data = self.cur.fetchone()
        self.cur.close()
        self.conn.close()
        return data

sql = 'select * from phonelist where age=%s'
params=(13)
my = getData()
data = my.execsql(sql, params)
print data