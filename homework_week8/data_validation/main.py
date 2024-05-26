from fastapi import FastAPI, Request, Form,Query, Body
from fastapi.responses import HTMLResponse,RedirectResponse,JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector
from pydantic import BaseModel
import re
from fastapi.middleware.cors import CORSMiddleware

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test",
)

mycursor = mydb.cursor()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許的來源列表
    allow_credentials=True,
    allow_methods=["*"],  # 允許的HTTP方法
    allow_headers=["*"],  # 允許的HTTP標頭
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(SessionMiddleware, secret_key = 'test', https_only = True)

templates = Jinja2Templates(directory="templates")

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
async def login_success(request: Request,page: int = Query(1, alias="page")):
    messages_per_page = 10
    offset = (page - 1) * messages_per_page
    print("Session:", request.session)
    if request.session.get("logged_in") == True:
        member_name = request.session.get("member_name")
        member_id = request.session.get("member_id")
        mycursor.execute("""
        SELECT website.member.name, website.message.content,website.message.member_id,website.message.id
        FROM website.message
        INNER JOIN website.member ON website.message.member_id = website.member.id
        """)

        messages = mycursor.fetchall()
        response = templates.TemplateResponse("login_sucess.html", {
            "request": request,
            "message": member_name,  
            "comment": messages,
            "member_id": member_id 
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
    request.session["logged_in"] = False
    print("Session:", request.session)
    return RedirectResponse(url="/")

password_pattern = re.compile(r'^[A-Za-z0-9@#$%]{4,8}$')

@app.post("/signup", response_class=HTMLResponse)
async def signup(signup_name: Optional[str] = Form(None), signup_username: Optional[str] = Form(None), signup_password: Optional[str] = Form(None)):
    mycursor.execute("SELECT COUNT(*) FROM website.member WHERE username = %s", (signup_username,))
    if mycursor.fetchone()[0] > 0:
        error_message = "Repeated username"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=303)
    elif not password_pattern.match(signup_password):
        error_message = "Password must be 4-8 characters long and include only English alphabets, numbers, and @#$%"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=303)
    else:
        sql = "INSERT INTO `website`.`member` (name, username, password) VALUES (%s, %s, %s)"
        val = (signup_name, signup_username, signup_password)
        mycursor.execute(sql, val)
        mydb.commit()
        return RedirectResponse(url="/", status_code=303)
    
@app.post("/createMessage", response_class=HTMLResponse)
async def comment(request: Request,comment: Optional[str] = Form(None)):
    if request.session.get("logged_in") == True:
        sql = "INSERT INTO `website`.`message` (content, member_id) VALUES (%s, %s)"
        member_id = request.session['member_id'] 
        val = (comment,member_id)
        mycursor.execute(sql, val)
        mydb.commit()
        return RedirectResponse(url="/member", status_code=303)
    else:
        return RedirectResponse(url="/")

@app.post("/deleteMessage", response_class=HTMLResponse)
async def delete(request: Request,message_id: Optional[str] = Form(None)):
    if request.session.get("logged_in") == True:
        message_id_int=int(message_id)
        if message_id:
            print("選取的留言ID是:", message_id_int)
        mycursor.execute("SELECT member_id FROM website.message WHERE id = %s", (message_id_int,))
        message_owner_id = mycursor.fetchone()
        current_user_id = request.session.get('member_id')
        if message_owner_id[0] == current_user_id:
            sql = "DELETE FROM website.message WHERE id = %s"
            val = (message_id_int,)
            mycursor.execute(sql, val)
            mydb.commit()
            return RedirectResponse(url="/member", status_code=303)
    else:
        return RedirectResponse(url="/")

class myResponse(BaseModel):
    id: int
    name: str
    username: Optional[str] = None

@app.get("/api/member", response_class=JSONResponse)
async def search_member(request: Request,username:Optional[str] = Query(None)):
    mycursor.execute("SELECT id,name FROM website.member WHERE username = %s", (username,))
    user_record = mycursor.fetchone()
    if request.session.get("logged_in") == True and user_record:
        member_id, member_name = user_record
        data = myResponse(id = member_id, name = member_name, username = username)
        response = {
            "data":data
            }
        return response
    elif not user_record or not request.session["logged_in"]:
        response = {
            "data":None
            }
        return response

class NameUpdate(BaseModel):
    name: Optional[str]

@app.patch("/api/member", response_class=JSONResponse)
async def new_name(request: Request,newname:NameUpdate = Body(...)):
    username = request.session.get('member_username')
    name = newname.name
    if request.session.get("logged_in") == True:
        mycursor.execute("UPDATE website.member SET name = %s WHERE username = %s", (name,username))
        mydb.commit()
        if mycursor.rowcount > 0:
            return {"ok":True}
        else:
            return {"error":True}
    else:
        return {"error":True}

