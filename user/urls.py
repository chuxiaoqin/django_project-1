from django.conf.urls import url
from  . import  views
app_name='user'
urlpatterns = [

    url(r'^login/', views.login, name='job'),
    url(r'^regist/', views.regist, name='regist'),
    url(r'^isExist/', views.isExist, name='isExist'),
    #验证token
    url(r'verify/',views.verifyToken),


    url(r'^show\w*', views.showMessage),
    url("setcookie/", views.setcookie),
    #通过公司id获取管理团队
    url(r"getmanagerbyid/(?P<cid>\w+)",views.getManagerById),
    # 通过username获取用户id
    url(r'getuseridbyname/(?P<username>\w+)', views.getUserIdByName),
    url(r'getdeliveryrecordbyid/', views.getDeliveryRecordByid),



]
