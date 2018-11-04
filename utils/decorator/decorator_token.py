from ..token.util_token import *
from  flask import  blueprints,request,jsonify
'''
def decotatorName(func):
    def wapper():
       
        return func()
    return wapper



'''
def checkToken(func):
    def wapper():
        try:
          token=request.header['token']
          res=deToken(token)
          return func(res)
        except jwt.ExpiredSignatureError as err:
            print("erroing.................", err)
            decode = {"error_msg": "is timeout !!", "some": None}
            res={"code":"004"}

        except Exception:
            decode = {"error_msg": "noknow exception!!", "some": None}
            print("erroing2.................")
            res = {"code": "004"}



        res["res"] = decode
        res["url"] = request.url
        return jsonify(res)  # 此处需要改进哦

    return wapper

#判断用户是否存在

def isExist(func):
    def wapper(userid):
        conn = None
        cursor = None
        try:
            conn = connect_mysql.connect()
            cursor = conn.cursor()

            sql = "select * from  user where  userid='{0}' ".format(userid)

            cursor.execute(sql)
            res = cursor.fetchall()
            print(res)
            res = True if res else False
        except Exception as ex:
            print(ex)
            res = False

        cursor and cursor.close()
        conn and conn.close()
        return res



        return func()

    return wapper
