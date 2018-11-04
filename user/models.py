from django.db import models
from  company.models import companys

# Create your models here.
#用户账户表
class user(models.Model):
    id = models.AutoField(primary_key=True)
    user_tel=models.CharField(unique=True,max_length=30)
    user_pwd=models.CharField(max_length=255)
    regist_date=models.DateTimeField(auto_now_add=True)


#hr表
class hr(models.Model):
    id = models.AutoField(primary_key=True)
    hr_tel=models.CharField(unique=True,max_length=30)
    hr_pwd=models.CharField(max_length=255)
    hr_date=models.DateTimeField(auto_now_add=True)
#公司管理团队表
class manager(models.Model):
    m_id=models.AutoField(primary_key=True)
    m_name=models.CharField(max_length=30,null=False)
    m_img=models.CharField(max_length=200)
    #管理人的职务
    m_position=models.CharField(max_length=50)
    #简介
    m_intro=models.TextField(max_length=1000)
    company = models.ForeignKey(companys, on_delete=models.CASCADE)