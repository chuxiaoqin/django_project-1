from django.shortcuts import render,HttpResponse
from position.models import positions,poslals,position_collection
from  user.models import manager
from .models import positions
from  company.models import addr,companys
from django.core.serializers import  serialize
from mongodb import mongo_posiiotn
from  django.http import JsonResponse

import  json
import pymongo
import re

# Create your views here.

#获取所有岗位
def getPositions(request):
   list_positions=[]
   pos =positions.objects.all()
   for p in pos:
       company=companys.objects.filter(c_id=p.company_id).select_related()[0]
       p=p.__dict__ #将model 对象转化为字典
       company=company.__dict__
       del p['_state'] #删除多余的字段
       del company['_state']
       position={
           "position":p,
           "company":company
       }

       list_positions.append(position)
       # print(company)
   # print(position)
   # print(list_positions)
   return HttpResponse(json.dumps(list_positions))

# #通过条件获取岗位（未处理）
# def getPositionsByCon(request,index,con=''):
#     # 条件和页码
#     index=1
#     data = mongo_posiiotn.getPositionsByCon(con)
#     print(data)
#     return HttpResponse(json.dumps(data))
#通过公司id获取岗位
def getPositionsByCid(request,cid):
    data_positions=[]
    pos=positions.objects.filter(company_id=cid)
    for p in pos :
        p=p.__dict__
        del p['_state']
        data_positions.append(p)
        # print(p)


    return HttpResponse(json.dumps(data_positions))
#通过岗位id获取岗位信息
def getPositionByPid(request,pid):
    pos=positions.objects.get(p_id=pid)
    com=pos.company
    com=com.__dict__
    pos=pos.__dict__
    # com_name=com.c_name
    #删除不需要的字段
    del com['_state']
    del pos['_state']
    # print(com)
    # print(pos)
    data={
        'position':pos,
        'company':com
    }

    return JsonResponse(data)
    pass
#获取标签
def gteLals(request):

    # data=mongo_posiiotn.getLals()
    # print(data)
    data_list=[]
    datas=poslals.objects.all()
    for data in datas:
        data={
            'id':data.id,
            'category_list_type':data.category_list_type,
            'category_list_hot':data.category_list_hot,
            'menu_sub':data.menu_sub
        }
        data_list.append(data)
    return HttpResponse(json.dumps(data_list))

#收藏岗位
def PositionsCollect(request):

    opetate=request.GET.get('operation')
    uid=request.GET.get('uid')
    pid=request.GET.get('pid')

    #如果操作时add的时候 向表中添加一条数据
    if opetate=='add':
        #先判断是否已经收藏了
        collected=position_collection.objects.filter(user_id=uid,position_id=pid)
        if collected:
            result={'result':'collected'}
        else:
            position_collection.objects.create(**{"user_id":uid,'position_id':pid})
            result = {'result': '200'}

    else:
        result={'result':'faild'}
    print(opetate)
    return JsonResponse(result)

#通过条件获取岗位 by gm
def getPositionsByCon(request,index,con):
    # 条件和页码
    pagesize=20
    index=int(index)
    list=[]
    data = mongo_posiiotn.getPositionsByCon(con)
    list.append(data[(index-1)*pagesize:pagesize*index])
    return HttpResponse(list)

#获取所有岗位 by gm
def getAllPositions(request):
    # 条件和页码
    list=[]
    data = mongo_posiiotn.getPositions()
    list.append(data)
    return HttpResponse(list)


#获取页码 by gm
def getPage(request,con):
    data=mongo_posiiotn.getPositionsByCon(con)

    len1=len(data)

    return JsonResponse({'acount':len1})

#存数据 不是正式的方法 个人测试使用--
def Save(request):

    try:
        uri = "mongodb://admin:123@127.0.0.1:27017/admin"
        client = pymongo.MongoClient(uri)

        # 2.操作的数据库
        db = client.test


    except Exception as  ex:
        print(ex)

    # 获取数据

    def getCompanys():
        companys = db.company_details.find()
        data_company = []
        for c in companys:
            del c['_id']
            data_company.append(c)
        return data_company

    def getPositions():

        positions = db.positions.find()

        data_positions = []

        for po in positions:
            del po['_id']
            data_positions.append(po)

        return data_positions

    def getLals():

        lals = db.lals.find()
        data_lals = []
        for lal in lals:
            del lal['_id']
            data_lals.append(lal)
        return data_lals

    pos = getPositions()
    data_companys = getCompanys()
    data_lals=getLals()

    # for p in pos :
    #     po={
    #        "p_name":p['position'],
    #        "p_id":p['pid'],
    #        "hr_id":p['hrid'],
    #        "img_url":p['img_url'],
    #        "salary":p['salary'],
    #         "pub_date":p['pub_date'].split('发布')[0],
    #        "exp":p['exp'],
    #        "edu":p['edu'],
    #        "word_cut":p['word_cut'],
    #        "company_id":p['cid']
    #
    #
    #     }
    #     try:
    #         positions(**po).save()
    #     except Exception as ex :
    #         print('此条记录添加失败')
    #
    # for co in data_companys:
    #     try:
    #         company={
    #             'c_id':co['cid'],
    #             'c_name':co['c_name'],
    #             'c_allname':co['all_name'],
    #             'img_src':co['img_src'],
    #             'href':co['href'],
    #             'c_word':co['company_word'],
    #             'type':co['type'],
    #             'rongzi':co['rongzi'],
    #             'size':co['size'],
    #             'c_lals':co['company_lals'].replace('\n',','),
    #             'position_number':re.search(r'\d+',co['data'][0]).group()if re.search(r'(\d+)',co['data'][0])  else 0,
    #             'jl_timeliness':re.search(r'(\d+)',co['data'][1]).group(1) if re.search(r'(\d+)',co['data'][1])  else 0 ,
    #             'jl_processing_time':co['data'][2],
    #             'mspj':re.search(r'\d+',co['data'][3]).group()if re.search(r'(\d+)',co['data'][3])  else 0,
    #             'last_login':co['data'][4],
    #             'addr_heade':co['addr_head'],
    #
    #             'intro':co['intro']
    #
    #
    #         }
    #         print(co['data'][1])
    #         for index in range(0,len(co['addrs_1'])):
    #             data_addr={
    #                 'addr_shi': co['addrs_1'][index],
    #             'addr_particular':co['addrs_2'][index],
    #                 'company_id': co['cid'],
    #
    #
    #             }
    #
    #         addr(**data_addr).save()
    #         for ma in co['manager']:
    #             data_manager={
    #                 "m_name":ma['name'],
    #                 "m_img":ma['img'],
    #                 "m_position":ma['positions'],
    #                 "m_intro":ma['intro']
    #
    #                    }
    #             data_manager["company_id"] =co['cid']
    #             manager(**data_manager).save()
    #         # companys(**company).save()
    #     except Exception as ex :
    #         print(ex)

    for l in data_lals:
        lal={
            "category_list_type":l['category_list_h2'],
            "category_list_hot":l['category_list_a'],
            "menu_sub":l['menu_sub']

        }
        poslals(**lal).save()


    return HttpResponse(json.dumps(pos))






































