from django.db import models
from position.models import positions
from user.models import user
# Create your models here.
#简历表
class resume(models.Model):

    id=models.AutoField(primary_key=True)
    #外键 简历所属用户
    user=models.ForeignKey(user,on_delete=models.CASCADE,default='')
    #后续字段自己再添加


#投递简历表
class position_and_resuem(models.Model):

    id=models.AutoField(max_length=30,primary_key=True)
    #岗位
    position=models.ForeignKey(positions,on_delete=models.CASCADE)
    #简历
    resume=models.ForeignKey(resume,on_delete=models.CASCADE)
    #auto_now_add 只在添加记录是更新后面的修改不会更新
    #auto_now 在修改时会更新
    #投递简历的时间
    pr_date=models.DateTimeField(auto_now_add=True)


#用户信息表
class userinfo(models.Model):
    id=models.AutoField(primary_key=True)#默认生成
    name=models.CharField(max_length=30)
    sex = models.CharField(max_length=30,choices=(('male', '男'), ('female', '女')), default='male')
    birthday=models.DateField(auto_now=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    #婚姻状态
    marital_status=models.CharField(max_length=30,choices=(('married', '已婚'), ('unmarried', '未婚')), default='male')
    #毕业院校
    graduation=models.CharField(max_length=100)
    #最高学历
    highest_education=models.CharField(max_length=50)
    #手机号码
    telephone=models.CharField(max_length=20)
    #email
    email = models.CharField(max_length=50)
    #目前居住地
    present_address=models.CharField(max_length=200)
    #所属的简历
    resume=models.ForeignKey(resume,on_delete=models.CASCADE)

#教育经历表

class education(models.Model):
   id=models.AutoField(primary_key=True)

   school_name=models.CharField(max_length=100)
   #专业
   profession=models.CharField(max_length=100)
   #开始日期
   begin_date=models.DateField(auto_now=True)
   #结束日期
   end_date=models.DateField(auto_now=True)
   #所属简历
   resuem=models.ForeignKey(resume,on_delete=models.CASCADE)


#工作经历表
class work_experience(models.Model):
    id = models.AutoField( primary_key=True)
    company_name=models.CharField(max_length=200)
    #岗位
    position_name=models.CharField(max_length=200)
    begin_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=True)
    #部门
    department=models.CharField(max_length=100)
    #工作内容
    work_content=models.TextField(max_length=1000)
    #专业
    profession=models.CharField(max_length=100)
    #所属简历
    resume=models.ForeignKey(resume,on_delete=models.CASCADE)

#项目经历表


#其他信息表
class other_message(models.Model):
    id = models.AutoField(primary_key=True)
    self_evaluation=models.TextField(max_length=1000)
    hobbies=models.TextField(max_length=1000)
    features=models.TextField(max_length=1000)
    resuem=models.ForeignKey(resume,on_delete=models.CASCADE)