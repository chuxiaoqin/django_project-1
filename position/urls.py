from  django.conf.urls import url

from . import  views

app_name='position'

urlpatterns=[

    # 通过条件获取所有岗位
    url(r'getpositionsbycon\w*/(?P<index>\d*)/(?P<con>.*)/', views.getPositionsByCon, name='getpositionsbycon'),

    # 获取页码
    url(r'getPage\w*/(?P<con>\w*)/', views.getPage, name='getPage'),

    # 获取岗位
    url(r'getpositions/',views.getPositions),

    #通过条件获取岗位（未完成）
    # url('getpositionsbycon/(?P<index>\d+)/(?P<con>\w+)',views.getPositionsByCon),
    #查找公司的所有岗位
    url('getpositionsbycid/(?P<cid>\d+)',views.getPositionsByCid),
    url('getpositionbypid/(?P<pid>\d+)',views.getPositionByPid),

    #获取所有岗位
    url(r'getAllpositions/',views.getAllPositions),


    # 获取岗位标签
    url(r'getlals/',views.gteLals),
    #收藏岗位添加记录
    url(r'savecollection/',views.PositionsCollect),

    url(r'getlals/',views.gteLals),

    #保存数据（mongodb 到 mysql  ）
    url('save',views.Save),


]
