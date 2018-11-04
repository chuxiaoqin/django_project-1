from django.db import models

# Create your models here.
class companys(models.Model):
    #公司id
    c_id=models.CharField(max_length=30,primary_key=True)
    #公司名称
    c_name=models.CharField(max_length=50)
    #公司全称
    c_allname=models.CharField(max_length=50)
    #图片链接
    img_src=models.CharField(max_length=200)
    #公司官网链接
    href=models.CharField(max_length=200)
    #公司关键词
    c_word=models.CharField(max_length=200)
    #公司类型
    type=models.CharField(max_length=100)
    #融资情况
    rongzi=models.CharField(max_length=50)
    #公司规模
    size=models.CharField(max_length=50)
    #公司标签
    c_lals=models.CharField(max_length=200)
    #在招岗位数量
    position_number=models.IntegerField()
    #简历处理及时率
    jl_timeliness=models.IntegerField()
    #简历处理用时
    jl_processing_time=models.CharField(max_length=50)
    #面试评价
    mspj=models.IntegerField()
    #最后一次登录
    last_login=models.CharField(max_length=50)
    #公司的主要地址
    addr_heade=models.CharField(max_length=200)

    # 公司简介
    intro=models.TextField(max_length=1000)

# 公司地址(多个地址)
class addr(models.Model):

    a_id=models.AutoField(primary_key=True)
    # 市
    addr_shi = models.CharField(max_length=200)
    # 详细地址
    addr_particular = models.CharField(max_length=200)
    #公司id
    company = models.ForeignKey(companys,on_delete=models.CASCADE)

