from  django.conf.urls import url

from . import  views

app_name='resume'

urlpatterns=[


    # 投递简历
    url('commit/',views.commitResuem),
    url('getresumesbyuid/',views.getResuemsByuid),
    url('createresume/',views.createResuem),
    url('modifyresume/',views.modifyResume),
    url('deleteresume/',views.deleteResume),
    url('addresume/',views.addResume)

]
