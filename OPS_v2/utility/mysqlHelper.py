#! _*_ coding: utf-8 _*_

import pymysql
from config.conf import conn_mysql_dict

class MysqlHelper(object):
    def __init__(self):
        self.__conn = conn_mysql_dict

    def getDict(self, sql, params=("")):
        conn = pymysql.connect(**self.__conn)
#         cur = conn.cursor(pymysql.cursors.DictCursor)
        cur = conn.cursor()

        retCount = cur.execute(sql)
        data = cur.fetchall()

        cur.close()
        conn.close()
        return data

    def getOne(self, sql, params):
        conn = pymysql.connect(**conn_mysql_dict)
        cur = conn.cursor()

        reCount = cur.execute(sql, params)
        data = cur.fetchone()

        cur.close()
        conn.close()
        return data