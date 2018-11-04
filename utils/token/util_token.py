import  jwt
from datetime import  datetime,timedelta


#设置秘钥
SECRECT_KEY="pdd"
#签发token
def getToken(telephone,id):

    #设置过期时间
    datetimeInt =datetime.now() +timedelta(seconds=180)
    option = {
         'iss':'app',
         'exp': datetimeInt,
         'aud':'webkit',
         'user': telephone,
        'id':id,
        'statuscode':'200'
    }
    token= jwt.encode(option, SECRECT_KEY, algorithm='HS256')
    return token


#解析token
def deToken(token):
    res= None
    try:
        res = jwt.decode(token, SECRECT_KEY, audience='webkit', algorithm='HS256')

    except Exception as ex:
        print(ex)
        res = {"statuscode": "400"}
        print("解析失败")



    return res


#测试
if __name__ == '__main__':
    print(deToken(getToken('002')))



