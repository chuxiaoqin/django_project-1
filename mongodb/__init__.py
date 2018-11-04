import  pymongo

try:
    uri = 'mongodb://127.0.0.1:27017/test'
    client=pymongo.MongoClient(uri)

    #2.操作的数据库
    db=client.test


except Exception as  ex:
    print(ex)