from . import *
'''
公司数据的操作

'''

def getCompanyById(cid):
   # c_name='给赞科技'
   company=[]
   companys= db.company_details.find({'cid':cid})#.pretty()
   for c in companys:
      del c['_id']
      company.append(c)
   #拿到的是集合得取出来

   print(company[0])
   return  company[0]

def getCompanys():
    companys=db.company_details.find()
    data_company=[]
    for c in companys:
        del c['_id']
        data_company.append(c)
    return data_company