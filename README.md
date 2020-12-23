# python 连接常见数据库并查询（使用步骤如下）

# 1. 根据数据库类型导入连接对应数据库包,修改代码中对应代码

## （1）mysql数据库：
#### import pymysql
#### self.dbconn = pymysql.connect(host=hostname, user=username, password=password, database=database, port=port)


## （2）postgres数据库：
#### import psycopg2
#### self.dbconn = psycopg2.connect(host=hostname, user=username, password=password, database=database, port=port)


## （3）sql server数据库：
#### import pymssql
#### self.dbconn = pymssql.connect(host=hostname, user=username, password=password, database=database, port=port)


## （4）Azure SQL 数据库( __init__中的连接数据库需使用注释的语句连接)
#### import pyodbc
#### self.dbconn = pyodbc.connect('DRIVER={SQL Server};SERVER='+hostname+';DATABASE='+database+';UID='+username+';PWD='+ password)


# 2. 配置数据库相关信息
#### hostname = ''
#### database = ''
#### username = ''
#### password = ''


# 3. 修改数据库查询语句 sql2

# 4.查询数据库
#### 使用： query_sql(sql2) 

