# python 查询不同数据库

#使用方法

# 1. 根据数据库类型更改导入连接数据库包，配置数据库相关信息（更改数据库之后需要修改DB类中 __init__数据库连接）
## （1）mysql数据库：
### import pymysql

## （2）postgres数据库：
### import psycopg2

## （3）sqlserver数据库：
### import pymssql

# 2. 配置数据库相关信息
#### hostname = ''
#### database = ''
#### username = ''
#### password = ''

# 3. 修改数据库查询语句 sql2

# 4.查询数据库
### 使用： query_sql(sql2) 

