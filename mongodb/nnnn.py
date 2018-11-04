import pymongo
uri = 'mongodb://127.0.0.1:27017/pdd'
client = pymongo.MongoClient(uri)

# 2.操作的数据库
db = client.pdd

con="仓库管理员"
positions = db.positions.find() if not con else db.positions.find({ "position":con})


data_positions=[]

for po in positions:
    del po['_id']
    data_positions.append(po)

print(data_positions[1:5])