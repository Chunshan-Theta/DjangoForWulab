#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)                         # 2
sys.setdefaultencoding('utf-8')     # 3



# 引入 MySQLdb 模組，提供連接 MySQL 的功能
import MySQLdb

# 連接 MySQL 資料庫
#db = MySQLdb.connect(host="xxx.xxxx.xxxx.xxxx",user="root", passwd="root_password", db="db_liat_name",charset='utf8')


print "-- DB commend: test connent to DB "
db = MySQLdb.connect(host="localhost",user="root", passwd="root", db="BSA",charset='utf8')
cursor = db.cursor()
print "-- DB commend: close test connection to DB"
db.close()

def status():
    if db.open:
        print '-- DB status: connection is open'
    else:
        print '-- DB status: connection is closed'

def connectDB(Thost="localhost",Tuser="root", Tpasswd="root", Tdb="BSA",Tcharset='utf8'):
    print "-- DB commend: connent to DB "+str(Thost)
    global db,cursor
    db = MySQLdb.connect(host=Thost,user=Tuser, passwd=Tpasswd, db=Tdb,charset=Tcharset)
    cursor = db.cursor()

def close():
    print "-- DB commend: close connection to DB"
    db.close()

def exeSQl(sql):
    print '-- SQL commend: '+str(sql)
    # 執行 MySQL 查詢指令
    cursor.execute(sql)

    # 取回所有查詢結果
    results = cursor.fetchall()
    '''
    # 輸出結果
    for record in results:
        row = ""
        for col in record:
            row += str(col).replace("\n", "")
            row += ","        
        print row
    '''
    return results

  

    








