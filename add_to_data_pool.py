# add data to data_pool
# add data to data_entry

import mysql.connector
from datetime import datetime
import time
from hashlib import sha256

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="blockchain_db"
)


cursor = mydb.cursor(buffered=True)

# loop get result
stop = False
while not stop :
    # add data to data entry
    data = str(input("Data : "))
    now = datetime.now().replace(microsecond=0)
    # mysql
    sql = 'Insert into data_entry (data, time) VALUES (%s, %s)'
    val = (data, now.strftime('%Y-%m-%d %H:%M:%S'))
    cursor.execute(sql, val)
    mydb.commit()
    time.sleep(2)
    con = str(input('Repeat (Y/N) : '))
    if con == 'N' :
        stop = True

# add all data from data_entry to data_pool
sql = "SELECT id,data, time FROM data_entry ORDER BY time"
cursor.execute(sql)
myresult = cursor.fetchall()


# get last id
# check if data pool empty
sql = """SELECT count(*) as tot FROM data_pool"""
cursor.execute(sql)
myres = cursor.fetchone()[0]
latestId = float('nan')
if myres != 0 :
    sql = """Select id from data_pool order by id desc"""
    cursor.execute(sql)
    resId = cursor.fetchone()[0]
    latestId = resId
else :
    sql = """Select id from blockchain_final order by id desc"""
    cursor.execute(sql)
    resId = cursor.fetchone()[0]
    latestId = resId


for i in myresult :
    #cursor = mydb.cursor()
    latestId += 1
    sql2 = """SELECT count(*) as tot FROM data_pool"""
    cursor.execute(sql2)
    dt = cursor.fetchall()[0][0]
    print('Total data in data pool : %s' % str(dt+1))
    prevHash = str(0)
    if dt != 0 :
        sql2 = """Select hash from data_pool order by id desc"""
        cursor.execute(sql2)
        prevHash = str(cursor.fetchone()[0])
    else :
        sql2 = """Select hash from blockchain_final order by id desc"""
        cursor.execute(sql2)
        prevHash = str(cursor.fetchone()[0])

    # hasing the block

    dictDt = {'id' : latestId,
              'prevHash' : prevHash,
              'data' : i[1],
              'time' : i[-1]}

    hashing = sha256(str(dictDt).encode('utf-8')).hexdigest()

    dictDt_final  = {'id' : latestId,
              'prevHash' : prevHash,
              'data' : i[1],
              'time' : i[-1],
              'hash' : hashing}

    sql = """Insert INTO data_pool (id, prevHash, data, time, hash) values (%s, %s, %s, %s, %s)"""
    val = (str(dictDt_final['id']), str(dictDt_final['prevHash']), str(dictDt_final['data']), str(dictDt_final['time']), str(dictDt_final['hash']))
    cursor.execute(sql, val)
    mydb.commit()

    sql = "DELETE FROM data_entry WHERE id = %s" % i[0]
    cursor.execute(sql)
    mydb.commit()

mydb.close()