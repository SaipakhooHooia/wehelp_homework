import mysql.connector
import time
from mysql.connector.pooling import MySQLConnectionPool

# 建立資料庫連接
db = {
    "host": "localhost",
    "user": "root",
    "password": "test",
    "database": "test",
}

#cursor.execute("CREATE INDEX idx_name_username ON test.member (username)")

pool = MySQLConnectionPool(pool_name="mypool", pool_size=5, **db)

connection = pool.get_connection()

sql_query = "SELECT * FROM member WHERE username LIKE '%UvQTqf'"

try:
    # 執行資料庫操作
    start_time = time.time()
    cursor = connection.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchall()
    print(result)
    end_time = time.time()
finally:
    # 使用後將連接返回給連接池
    connection.close()

# 輸出查詢花費時間
print(f"Query executed in {end_time - start_time} seconds")

#DROP INDEX idx_name_username ON member;
#SELECT * FROM member WHERE username LIKE 'test%';