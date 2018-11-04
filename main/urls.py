"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from  . import  views
from django.conf.urls import url
import  user.urls
import  company.urls
import  position.urls
import resume.urls
urlpatterns = [
    #主路由
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),


    #子路由
    url(r'^user/',include(user.urls,namespace='user')),
    url(r'company/',include(company.urls ,namespace='company')),
    url(r'position/',include(position.urls,namespace='position')),
    url(r'resume/',include(resume.urls,namespace='resume'))

]
