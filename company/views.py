# Create your views here.
from django.shortcuts import render
from  django.http import  HttpResponse
from  mongodb import mongo_company
from  .models import  companys,addr
from django.core.serializers import  serialize
import json

#通过公司id获取公司信息
def getCompanyById(request,cid):
    if request.method == 'GET':
        # print(cid)
        cid=cid or "43055"
        # print(cid)
        data=serialize('json',companys.objects.filter(c_id=cid),ensure_ascii=False)
        data=eval(data)#将str转换为字典列表
        # data=data[0]#取出第一个数据
        # data=data['fields'] #取出fields字段

    else:
        data = {"statuscode": 400}

    # print( data['fields'])
    data=data[0]
    return  HttpResponse(json.dumps(data))

#通过公司id获取公司地址
def getAddrById(request,cid):
    if request.method == 'GET':
        # print(cid)
        cid=cid or "43055"
        # print(cid)
        data =serialize('json',addr.objects.filter(company_id=cid),ensure_ascii=False)

    else:
        data = {"statuscode": 400}

    # print(data)

    return  HttpResponse(json.dumps(data))

#获取公司信息
def getCompanys(request):
    if request.method=='GET':
        #数量太多暂时取 30 条记录
        data=serialize('json',list(companys.objects.all()),ensure_ascii=False)
        #从mysql取到的数据基本上是str所以要处理一下
        data=eval(data)[0:90]
        print(type(data))
        # print(type(json.dumps(data)))
        return HttpResponse(json.dumps(data))