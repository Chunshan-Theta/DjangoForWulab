#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)                         # 2
sys.setdefaultencoding('utf-8')     # 3



# 引入 MySQLdb 模組，提供連接 MySQL 的功能
import MySQLdb

# 連接 MySQL 資料庫
#db = MySQLdb.connect(host="xxx.xxxx.xxxx.xxxx",user="root", passwd="root_password", db="db_liat_name",charset='utf8')
db = MySQLdb.connect(host="140.118.37.196",user="root", passwd="ytwu57874", db="ets_search",charset='utf8')
cursor = db.cursor()



def exeSQl(sql):
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

def ShowDBList(data):
    for record in data:
        row = ""
        for col in record:
            row += str(col).replace("\n", "")
            row += " | "        
        print row
        print '-'*10



############################

search_web = exeSQl("SELECT * FROM search_web")
note = exeSQl("SELECT * FROM note")
search = exeSQl("SELECT * FROM search")
chat_record = exeSQl("SELECT * FROM chat_record")           


#ShowDBList(note)                                           #show data of SQL list









