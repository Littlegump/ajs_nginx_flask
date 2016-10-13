# _*_ coding: utf-8 _*_

from utility.mysqlHelper import MysqlHelper

class Opr(object):
    def __init__(self):
        self.__helper = MysqlHelper()
        self.__sql = "select * from phonelist"

    def getAll(self):
        return self.__helper.getDict(self.__sql)

    def insertIterm(self, sql, params):
        pass