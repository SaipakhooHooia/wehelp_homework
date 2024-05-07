from fastapi import FastAPI, Request, Form,Query, Path
from fastapi.responses import HTMLResponse,RedirectResponse,JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test",
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
databases = []
for db in mycursor:
    databases.append(db[0])#db會返回一個tuple，因此要取tuple的第一個值

print(databases)
if "website" not in databases:
    mycursor.execute("CREATE DATABASE website")
    mycursor.execute("""CREATE TABLE `website`.`member` (
    `id` BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
    `name` VARCHAR(255) NOT NULL COMMENT 'Name',
    `username` VARCHAR(255) NOT NULL COMMENT 'Username',
    `password` VARCHAR(255) NOT NULL COMMENT 'Password',
    `follower_count` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',
    `time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time'
    );""")
    mycursor.execute("""CREATE TABLE website.message (
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
    member_id BIGINT NOT NULL COMMENT 'Member ID for Message Sender',
    FOREIGN KEY (member_id) REFERENCES member(id),
    content VARCHAR(255) NOT NULL COMMENT 'Content',
    like_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Like Content',
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time'
    );""")
    mydb.commit()
else:
    pass

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(SessionMiddleware, secret_key = 'test', https_only = True)

templates = Jinja2Templates(directory="templates")

login_data = {
    "username": "test",
    "password": "test"
}

message=["Please enter username and password","Username or password is not correct"]

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})

@app.post("/signin", response_class=HTMLResponse)
async def login(request: Request,username: Optional[str] = Form(None), password: Optional[str] = Form(None)):
    mycursor.execute("SELECT COUNT(name) FROM website.member WHERE username = %s AND password = %s", (username, password))
    if mycursor.fetchone()[0] > 0:
        mycursor.execute("SELECT id,name FROM website.member WHERE username = %s AND password = %s", (username, password))
        user_record = mycursor.fetchone()
        member_id, member_name = user_record
        request.session['member_name'] = member_name
        request.session['member_id'] = member_id
        request.session['member_username'] = username
        request.session["logged_in"] = True
        print("Session:", request.session)
        return RedirectResponse(url="/member", status_code=303)#使用status code 303可以讓瀏覽器重新發一個get request
    else:
        error_message = "Username or password is not correct"  # 自定義錯誤訊息
        return RedirectResponse(url=f"/error?message={error_message}", status_code=303)
    
@app.get("/member", response_class=HTMLResponse)  
async def login_success(request: Request):
    print("Session:", request.session)
    if request.session.get("logged_in") == True:
        member_name = request.session.get("member_name")
        mycursor.execute("""
        SELECT website.member.name, website.message.content
        FROM website.message
        INNER JOIN website.member ON website.message.member_id = website.member.id
        """)
        messages = mycursor.fetchall()
        response = templates.TemplateResponse("login_sucess.html", {
            "request": request,
            "message": member_name,  
            "comment": messages  
        })
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    else:
        return RedirectResponse(url="/")

@app.get("/error", response_class=HTMLResponse)  
async def login_fail(request: Request):
    error_message = request.query_params.get("message")
    print("error_message=", request.query_params.get("message"))
    print(request.url)
    return templates.TemplateResponse("login_fail.html", {"request": request, "message": error_message})

@app.get("/signout", response_class=HTMLResponse)
async def logout(request: Request):
    # 删除session数据
    request.session["logged_in"] = False
    print("Session:", request.session)
    return RedirectResponse(url="/")

@app.post("/signup", response_class=HTMLResponse)
async def signup(signup_name: Optional[str] = Form(None), signup_username: Optional[str] = Form(None), signup_password: Optional[str] = Form(None)):
    mycursor.execute("SELECT COUNT(*) FROM website.member WHERE username = %s", (signup_username,))
    if mycursor.fetchone()[0] > 0:
        error_message = "Repeated username"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=303)
    else:
        sql = "INSERT INTO `website`.`member` (name, username, password) VALUES (%s, %s, %s)"
        val = (signup_name, signup_username, signup_password)
        mycursor.execute(sql, val)
        mydb.commit()
        return RedirectResponse(url="/", status_code=303)
    
@app.post("/createMessage", response_class=HTMLResponse)
async def comment(request: Request,comment: Optional[str] = Form(None)):
    sql = "INSERT INTO `website`.`message` (content, member_id) VALUES (%s, %s)"
    member_id = request.session['member_id'] 
    val = (comment,member_id)
    mycursor.execute(sql, val)
    mydb.commit()
    return RedirectResponse(url="/member", status_code=303)