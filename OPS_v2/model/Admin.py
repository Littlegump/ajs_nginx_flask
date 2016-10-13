from utility.mysqlHelper import MysqlHelper

class Admin(object):

    def __init__(self):
        self.__helper = MysqlHelper()

    def getName(self, id): # this function needs id
        sql = "select * from admin where id=%s"
        params = (id,)
        return self.__helper.getOne(sql,params)

    def checkValidate(self, username, password):
        sql = "select * from admin where name=%s and passwd=%s"
        params = (username, password)
        return self.__helper.getOne(sql, params)

    # if this table is used for checkvalidate, then this function can do it by follow sentence


user = raw_input("username")
pwd = raw_input("password")
a = Admin()
result = a.checkValidate(user, pwd)
    if not result:
        print "user passwd error"
    else:
        print "into backend login page"