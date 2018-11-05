from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import  models
from  django.core.serializers import  serialize
import  json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import  models
from utils.token.util_token import *
from werkzeug.security import generate_password_hash,check_password_hash
from  .models import user
import  json
import re
import  resume.views
import  resume.models
import time
# Create your views here.
'''
此模块方法未测试
仅供参考
建议负责人重写

此模块 设计关于所有的人员信息和
操作

'''
def login(request):
    if request.method=='POST':
        telephone = json.loads(request.body.decode())['telephone']
        # print(type(telephone))
        password = json.loads(request.body.decode())['password']

        # print(password)
        res_password = list(models.user.objects.filter(user_tel=telephone).values())
        res_id=models.user.objects.filter(user_tel=telephone).values()[0]['id']
        print(res_id)
        # print(res_password)
        # print(res_password[0]['user_pwd'])
        try:
            if telephone and password  and password==res_password[0]['user_pwd']:
                res_token=getToken(telephone,res_id)
    #           生成token
                response = JsonResponse({"code": "205"})
                response["token"]=res_token
                response["Access-Control-Allow-Headers"] = "Token"
                response["Access-Control-Expose-Headers"] = "Token"
                return response
            else:
                # 密码不对
                return JsonResponse({"code":"405"})
        except Exception  as ex:
            print("错误是", ex)
    else:
        # 请求失败
        return JsonResponse({"code":"请求失败"})



def regist(request):
    if request.method=='POST':
        reg = r'^1[34578]\d{9}$'
        telephone=json.loads(request.body.decode())['telephone']
        # print(type(telephone))
        if re.match(reg, telephone):
            password = json.loads(request.body.decode())['password']
            try:
                if len(password) >= 6:
                    # password = generate_password_hash(password, method='pbkdf2:sha1:2000', salt_length=8)
                    print(password)
                    ins_user = {
                    "user_tel": telephone,
                    "user_pwd": password,
                    }
                    # print("要插入用户表的数据", ins_user)
                    res_in_user = models.user.objects.create(**ins_user)
                    # print(res_in_user)
                    # print("ins_user", ins_user)
                    res_token = getToken(ins_user)
                    # 生成token
                    response = JsonResponse({"code": "205"})
                    response["token"] = res_token
                    response["Access-Control-Allow-Headers"] = "Token"
                    response["Access-Control-Expose-Headers"] = "Token"
                    return response
                else:
                    # 密码不合法
                    return JsonResponse({"code": "511"})
            except Exception as ex:
                print("错误是", ex)
                return JsonResponse({"code": "405"})
        else:
            # 手机号不合法
            return JsonResponse({"code": "512"})
    else:
        # 请求失败
        return JsonResponse({"code": "请求失败"})



def isExist(request):
    if request.method=="POST":
        telephone=json.loads(request.body.decode())
        res=list(models.User.objects.filter(user_tel=telephone).values())
        print(res)
        if len(res)>0:
            # 用户已存在
            return JsonResponse({"code":"208"})
        else:
            # 用户不存在
            return JsonResponse({"code":"408"})
    else:
        # 请求失败
        return JsonResponse({"code":"510"})

#显示个人信息
def showMessage(reauest):

    return HttpResponse({'status':'200'})

#设置cookie
def setcookie(request):
    res = HttpResponse()
    cookie = res.set_cookie("sunck","nice")
    return res

#获取公司管理团队的信息(测试通过勿修改)
def getManagerById(request,cid):
    managers=[]
    #从mysql取出来的是str 要把外边的双引号去掉恢复为原来的数据格式
    data_mangers=eval(serialize('json',list(models.manager.objects.filter(company_id=cid)),ensure_ascii=False))
    #这里因为数据是从model里取出来，所以取出来的数据是model对象，取其中需要的数据fields (字段)
    for m in data_mangers:

        managers.append(m['fields'])
    # print(managers)
    #发送给前端
    return HttpResponse(json.dumps(managers))


#验证token
def verifyToken(request):
    if request.method=='POST':
        #拿到token
        token=json.loads(request.body)['token']
        #验证token
        result=deToken(token)

        # print(result)
    return HttpResponse(json.dumps(result))
#通过用户名获取用户 id

def getUserIdByName(request,username):
    u=serialize('json',user.objects.filter(user_tel=username))
    uid=eval(u)[0]['pk']
    # print(uid)

    return JsonResponse({'id':uid})

def getDeliveryRecordByid(request):
    if request.method=='GET':
        token=request.META.get('HTTP_TOKEN')
        # print(token)
    else:
        token = request.META.get('HTTP_TOKEN')
    result=deToken(token)

    if result['statuscode']and not result['statuscode'] == '400':
        #在token中获取用户信息
        uu=result['user']
        #获取用户id
        uid=user.objects.get(user_tel=uu).id
        #获取该用户的所有简历
        resumes=resume.models.resume.objects.filter(user__id=uid)
        data=[]
        for resu in resumes:

           records=resume.models.position_and_resuem.objects.filter(resume_id=resu.id)
           # print(list(records))

           # records=serialize('json',records)
           # records=eval(records)
           for r in list(records):
               if r:
                   del r.position.__dict__['_state']
                   del r.resume.__dict__['_state']
                   data_position=r.position.__dict__
                   data_resume=r.resume.__dict__
                   data_pr_date=str(r.pr_date)
                   record={
                       'id':r.id,
                       'position':data_position,
                       'resume':data_resume,

                       'pr_date':data_pr_date.split('.')[0]
                   }
                   # print(record)
                   # r=eval(serialize('json',r))
                   # del r['model']
                   # r['fields']['pr_date']=r['fields']['pr_date'].split('.')[0].replace('T',' ')

                   data.append(record)



        #根据id排序
        data=sorted(data,key=lambda x: x['id'])
        # print(data)


        # print(time.mktime(time.strptime(data[0]['fields']['pr_date'].split('.')[0].replace('T',' '),'%Y-%m-%d %H:%M:%S')))

    return HttpResponse(json.dumps(data))
