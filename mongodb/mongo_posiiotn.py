from . import *



#获取岗位
def getPositions():


    positions=db.positions.find()

    data_positions=[]

    for po in positions:
        del po['_id']
        data_positions.append(po)

    return data_positions


#根据条件查找岗位
def getPositionsByCon(con):


    positions = db.positions.find() if not con else db.positions.find({ "position" :'仓库管理员'})

    data_positions = []

    for po in positions:
        del po['_id']
        data_positions.append(po)

    return data_positions



#获取标签
def getLals():

    lals = db.lals.find()
    data_lals = []
    for lal in lals:
        del lal['_id']
        data_lals.append(lal)
    return data_lals





