# -*- coding: utf-8 -*-

#导入连接数据库包
import pymysql
import pandas as pd
#配置数据库信息
hostname = ''
database = ''
username = ''
password = ''
#数据库连接端口，如果不设置，则使用默认端口
port=0


class DB(object):
    def __init__(self):
        #连接数据库
        if not port:
            self.dbconn = pymysql.connect(host=hostname, user=username, password=password, database=database)
        else:
            self.dbconn = pymysql.connect(host=hostname, user=username, password=password, database=database,port=port)
        #获取游标
        self.dbcur = self.dbconn.cursor()
    def __enter__(self):
        return self.dbcur
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.dbconn.commit()
        self.dbcur.close()
        self.dbconn.close()

#查询数据库函数
def query_sql(sql):
    with DB() as db:
        result = db.execute(sql)
        data = db.fetchall()
        return data

#查询sql语句
sql2=''

#查询结果
result=query_sql(sql2)
#数据格式转换
df=pd.DataFrame(result)


