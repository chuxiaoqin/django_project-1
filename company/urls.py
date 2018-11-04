from  django.urls import path,include
from  django.conf.urls import url
from  . import views


app_name='company'

urlpatterns=[




    #通过id获取公司信息
    url(r'getcompanybyid/(?P<cid>\w+)',views.getCompanyById),
    #通过id获取公司地址
    url(r'getaddrbyid/(?P<cid>\w+)',views.getAddrById),
    #获取公司
    url(r'getcompanys/',views.getCompanys)




]
