import mysql.connector
from datetime import datetime, timedelta
import random
import string
import time

# 建立資料庫連接
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test",
    database="test",
    auth_plugin='mysql_native_password'
)

cursor = db.cursor()

# 定義插入語句
insert_query = "INSERT INTO `member` (`name`, `username`, `password`, `follower_count`, `time`) VALUES (%s, %s, %s, %s, %s)"

# 随机生成字符串的函数
def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# 产生一万笔测试资料并插入到数据库中
for i in range(100000):
    name = random_string(10)  # 随机生成10位字符作为name
    username = random_string(8)  # 随机生成8位字符作为username
    password = "testpass"
    follower_count = i
    # 使用当前日期时间加上迴圈数量的 timedelta 来生成不同时间的测试资料
    time = datetime.now() + timedelta(days=i, hours=i)
    data = (name, username, password, follower_count, time)
    cursor.execute(insert_query, data)

# 提交数据库变更
db.commit()

# 关闭数据库连接
cursor.close()
db.close()

print("100000 member datas are inserted.")

