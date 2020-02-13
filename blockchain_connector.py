port = 27017
mongo_addr = ('localhost', port)
#dbName = 'blockchain'
#colName = 'block'

dbName = 'business'
colName = 'reviews'

import pymongo
#client = MongoClient('localhost', port)
#db = client.blockchain

# addr = mongo_addr[0], port = mongo_addr[-1]
# addr, port
# https://stackoverflow.com/questions/28113947/how-to-properly-use-try-except-in-python
def createMongoclient (URI='mongodb://{0}:{1}'.format(mongo_addr[0], mongo_addr[1]) ) :
    conn = pymongo.MongoClient()
    print(URI)
    if conn is None :
        # no conn
        print("Mongo Server not found ... ? URI error")
        return
    #print('xxxxx')
    print('Server present ....')
    try :
     #   print('xdasdasdas')
      #  client = conn[dbName][colName]
      #  fivestarcount = client.find({})
      #  for dt in fivestarcount:
      #      print(dt)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to server: %s" % e)


def closeMongoClient (client:pymongo.MongoClient) :
    client.close()
    print("Client closed ....")

def openDB(client, dbName:str =dbName) :
    return client[dbName]

def openCollection(dtBase, col:str = colName) -> pymongo.collection :
    return dtBase[colName]


if __name__ == "__main__" :
    s = createMongoclient()
    #print('running')
    closeMongoClient(s)