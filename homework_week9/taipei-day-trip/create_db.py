import json
import mysql.connector
import re

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test",
)

mycursor = mydb.cursor()

# 打開JSON檔案並讀取數據
with open('data/taipei-attractions.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    pretty_json = json.dumps(data, indent=4)
    #print(pretty_json)

for item in data['result']['results']:
    pattern = r'https:\/\/.*?\.(?:jpg|png)'
    urls = re.findall(pattern, item['file'], re.IGNORECASE)
    for url in urls:
        print(url)

url_pattern = r'https:\/\/.*?\.(?:jpg|png)'

for item in data['result']['results']:
    check_sql = "SELECT COUNT(*) FROM `website`.`turist_spot` WHERE name = %s"
    mycursor.execute(check_sql, (item["name"],))
    urls = re.findall(url_pattern, item['file'], re.IGNORECASE)
    image_urls_json = json.dumps(urls)
    print(type(image_urls_json))
    if mycursor.fetchone()[0]>0:
        pass
    else:
        urls = re.findall(url_pattern, item['file'], re.IGNORECASE)
        sql = "INSERT INTO `website`.`turist_spot` (name, MRT, SERIAL_NO, file, description) VALUES (%s, %s, %s, %s, %s)"
        val = (item["name"],item["MRT"],item["SERIAL_NO"],image_urls_json, item["description"])
        mycursor.execute(sql, val)
        mydb.commit()