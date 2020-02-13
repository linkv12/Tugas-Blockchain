import blockchain_connector as bconn
import blockchain_structure as bstruct
import datetime

def getLastBLockHash(coll) :

    x = coll.find().limit(50).sort('_id')
    print(list(x))

def addBlock(data) :
    client = bconn.createMongoclient()
    block_collection = bconn.openCollection(
                    bconn.openDB(client))
    if block_collection.count_documents({}) == 0 :
        block_oid_genesis = block_collection.insert(bstruct.block(0, 'genesis', str(datetime.datetime.now()), '0').getDict())

    block_oid = block_collection.insert_one(bstruct.block(latest_index, data, datetime.datetime.now(), prevHash).getDict())
    if block_oid is not None :
        print("Success input : {0}".format(block_oid))
    bconn.closeMongoClient(client)

def getAllBlock():
    client = bconn.createMongoclient()
    block_collection = bconn.openCollection(
                    bconn.openDB(client))
    all_block = block_collection.find({})
    #print(list(list(all_block)[-1].values())[1:])
    temp_list = []

    for dt in all_block :
        #print('i')
        #print(list(dt.values())[1:])
        #print(list(dt.values())[1:])
        temp_list.append(list(dt.values())[1:])
    bconn.closeMongoClient(client)

    #print(temp_list)
    return temp_list

if __name__ == "__main__" :
    client = bconn.createMongoclient()
    coll = bconn.openCollection(
        bconn.openDB(client))
    getLastBLockHash(coll)
    client.close()
    #getAllBlock()