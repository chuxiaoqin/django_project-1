from  django.conf.urls import url

from . import  views

app_name='forum'

urlpatterns=[
#获取帖子
    url('/getcomments/',views.getComments)






]
