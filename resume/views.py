from django.shortcuts import render
from  utils.decorator.decorator_token import  checkToken
from resume.models import  position_and_resuem
from user.models import user
from resume.models import resume,userinfo
from  django.http import  HttpResponse
from utils.token.util_token import deToken
from . import models
import  json
# Create your views here.

#投递简历
def  commitResuem(request):
    position_id=request.GET.get('position_id')
    resume_id=request.GET.get('resume_id')
    iscommited=position_and_resuem.objects.filter(position_id=position_id,resume_id=resume_id)

    if not iscommited:
        data={
            'position_id':position_id,
            'resume_id':resume_id
        }

        position_and_resuem.objects.create(**data)

        result={
            'status': '200' #简历投递成功
        }
    else:
        result={
            'status':'403' #该简历已投递
        }


    # print(data)

    return HttpResponse(json.dumps(result))



#通过用户id获取简历

def getResuemsByuid(request):

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
        resumes=resume.objects.filter(user__id=uid)
        data=[]
        for resu in resumes:
            resu=resu.__dict__
            del resu['_state']

            data.append(resu)



    return HttpResponse(json.dumps(data))


#创建简历表(空的简历表)
def createResuem(request):
    #判断是否登录
    token=request.META.get('HTTP_TOKEN')

    uu=deToken(token)['user']
    uid=user.objects.get(user_tel=uu).id
    data_resume={
        'user_id':uid
    }
    l = len(resume.objects.filter(user_id=uid))
    #每个用户限制最多创建10个简历
    if l<10:
     resume.objects.create(**data_resume)
     #获取刚创建的简历的id
     resume_id=resume.objects.filter(user_id=uid)[l].id
     data_resume['resume_id']=resume_id

    else:
        data_resume={'status':400}
    return HttpResponse(json.dumps(data_resume))


#添加简历
def addResume(request):
    if request.method=='POST':
        try:
            token = json.loads(request.body)['token']
            uu = deToken(token)['user']

            print(uu)
            uid = user.objects.get(user_tel=uu).id
            data_resume = {
                'user_id': uid
            }

            l = len(resume.objects.filter(user_id=uid))
            resume.objects.create(**data_resume)

            resume_id = resume.objects.filter(user_id=uid)[l].id

            data_resume['resume_id'] = resume_id

            name =json.loads(request.body)['name']
            sex =json.loads(request.body)['sex']
            highest_education =json.loads(request.body)['highest_education']
            email =json.loads(request.body)['email']
            marital_status=json.loads(request.body)['marital_status']
            birthday =json.loads(request.body)['birthday']
            telephone =json.loads(request.body)['telephone']
            present_address =json.loads(request.body)['present_address']
            graduation =json.loads(request.body)['graduation']

            message={
                'name':name,
                'sex':sex,
                'highest_education':highest_education,
                'email':email,
                'marital_status':marital_status,
                'birthday':birthday,
                'telephone':telephone,
                'present_address':present_address,
                'graduation':graduation,
                'resume_id':resume_id,
                'user_id':uid
            }
            add_message =userinfo.objects.create(**message)
            return HttpResponse(json.dumps(data_resume))

        except Exception as ex:
            print(ex)
            return HttpResponse(json.dumps({'code':'500'}))

#修改简历
def modifyResume(request):
    pass

#删除简历
def deleteResume(request):
    pass


#简历的子表
# 工作经历
def createWorkExp(request):
    pass
# 教育经历
# 基本信息
# 其他信息
