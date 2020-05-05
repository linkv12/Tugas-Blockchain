from threading import Lock
from threading import Thread
import time
from datetime import datetime
import mysql.connector
from hashlib import sha256


semLock = Lock()

class block :
    def __init__(self,id,prevHash,data,time,hash ) :
        self.id = id
        self.prevHash = prevHash
        self.data = data
        self.time = time
        self.hash = hash
        self.diction = {'id': self.id,
                        'prevHash': self.prevHash,
                        'data': self.data,
                        'time': self.time,
                        'hash': self.hash}
    def get_hash_w_nonce(self, nonce):
        hash_nonce = 0
        dict2 = self.diction.copy()
        dict2['nonce'] = nonce
        hash_nonce = str(sha256(str(dict2).encode('utf-8')).hexdigest())
        return hash_nonce

    def dict_nonce(self, nonce):
        dict2 = self.diction.copy()
        dict2['nonce'] = nonce
        return dict2

found = False

class myThreadMining(Thread) :
    def __init__(self, id, name, blk:block):
        Thread.__init__(self)
        self.id = id
        self.name = name
        self.blk = blk

    def run(self):
        def calcNonce(blockObj : block) : # receive block object
            nonce = 0
            foundx = False
            while not foundx :
                # hash -> blockcahin + nonce
                hashedBlock = blockObj.get_hash_w_nonce(nonce)
                if hashedBlock[:4] == '0000' :
                    foundx = True
                nonce = nonce + 1
                global found
                if found == True :
                    foundx = True

            return nonce


        nonce = calcNonce(self.blk)
        global found
        found = True
        semLock.acquire()
        # init connection mysql
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="blockchain_db"
        )

        cursor = mydb.cursor(buffered=True)

        # delete data from data_pool
        sql = "DELETE FROM data_pool WHERE id = %s" % self.blk.id
        cursor.execute(sql)
        mydb.commit()

        # wheter it already added to final bloackchain
        sql2 = """SELECT count(*) as tot FROM blockchain_final where id = %s"""
        cursor.execute(sql2, (self.blk.id, ))
        myres = cursor.fetchone()[0]

        if myres == 0 :
            # input to blockchain table
            # add nonce extra
            dict_nonce = self.blk.dict_nonce(nonce)
            sql = """Insert INTO blockchain_final (id, prevHash, data, time, hash, nonce) values (%s, %s, %s, %s, %s, %s)"""
            val = (str(dict_nonce['id']), str(dict_nonce['prevHash']), str(dict_nonce['data']), str(dict_nonce['time']),
                   str(dict_nonce['hash']), str(dict_nonce['nonce']))
            cursor.execute(sql, val)
            mydb.commit()

        mydb.close()
        semLock.release()

def main() :
    # runn
    x = input("Run mine ? [Press Enter]  ")

    iter = 0
    stopage = True
    while stopage :
        global found
        found = False
        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="blockchain_db"
        )

        cursor2 = mydb2.cursor(buffered=True)
        sql2 = """SELECT count(*) as tot FROM data_pool"""
        cursor2.execute(sql2)
        dt = cursor2.fetchall()[0][0]

        # if list is not empty
        if dt != 0 :
            # create fetch an object
            sql3 = """Select * from data_pool order by id"""
            cursor2.execute(sql3)
            dt3 = cursor2.fetchone()


            # generate block

            blk = block(dt3[0],dt3[1],dt3[2],dt3[3],dt3[-1])
            #print(dt3)
            #print(blk.diction)

            thread_list = []
            for i in range(3):
                thread_list.append(myThreadMining(i, 'Thread-%s' % str(i+1), blk))

            for thr in thread_list :
                thr.start()

            # print all

            for thr in thread_list :
                thr.join()
        else :
            print("Data Pool : Empty")
            print('Waiting for data')
            time.sleep(1)
            iter += 1

        if iter > 100 :
            stopage = False

    print('Timeout, restart')

main()