from django.db import models
from  company.models import companys
from  user.models import user
# Create your models here.
#岗位表
class positions(models.Model):
    #岗位名称
    p_name=models.CharField(max_length=30,null=False)
    #岗位id
    p_id=models.CharField(max_length=50,primary_key=True)
    #hr id
    hr_id=models.CharField(max_length=30,null=False)
    #图片链接地址 因为没存地址所以就使用链接
    img_url=models.CharField(max_length=200)
    #发布日期
    pub_date=models.CharField(max_length=100)
    #工资
    salary=models.CharField(max_length=30,null=False)
    #经验要求
    exp=models.CharField(max_length=50)
    # 教育经历要求
    edu=models.CharField(max_length=50)
    #关键词
    word_cut=models.CharField(max_length=100)
    # 公司id 将设置为外键链接公司表
    company = models.ForeignKey(companys, on_delete=models.CASCADE)


# 公司标签
# class poslals_type(models.Model):
#     pt_id=models.IntegerField(auto_created=True,primary_key=True)
#     pt_type=models.CharField(max_length=200)
#
#
#     pass
#
# class poslals_hot(models.Model):
#     ph_id = models.IntegerField(auto_created=True, primary_key=True)
#     ph_hot=models.CharField(max_length=200)
#     pass
#
# class poslals_total(models.Model):
#     ptt_id=models.ph_id = models.IntegerField(auto_created=True, primary_key=True)
#     ptt_total=models.CharField(max_length=200)
#     pass

#岗位标签
class poslals(models.Model):
    category_list_type=models.CharField(max_length=200)
    category_list_hot=models.CharField(max_length=200)
    menu_sub=models.CharField(max_length=1000)

#岗位收藏
class position_collection(models.Model):
    #一条收藏记录id
    id=models.IntegerField(auto_created=True,primary_key=True)
    #收藏岗位id
    position=models.ForeignKey(positions,on_delete=models.CASCADE)
    #用户的id
    user=models.ForeignKey(user,on_delete=models.CASCADE)

