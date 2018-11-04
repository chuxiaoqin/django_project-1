def AAA():

    import  pymongo
    from position.models import *
    try:
        uri="mongodb://admin:123@127.0.0.1:27017/admin"
        client=pymongo.MongoClient(uri)

        #2.操作的数据库
        db=client.test


    except Exception as  ex:
        print(ex)
    #获取数据

    def getCompanys():
        companys=db.company_details.find()
        data_company=[]
        for c in companys:
            del c['_id']
            data_company.append(c)
        return data_company


    def getPositions():


        positions=db.positions.find()

        data_positions=[]

        for po in positions:
            del po['_id']
            data_positions.append(po)

        return data_positions

    def getLals():

        lals = db.lals.find()
        data_lals = []
        for lal in lals:
            del lal['_id']
            data_lals.append(lal)
        return data_lals

    pos = getPositions()
    companys = getCompanys()
    print(len(pos))
    print(len(companys))