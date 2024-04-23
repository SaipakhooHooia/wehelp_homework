from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(SessionMiddleware, secret_key = 'test', https_only = True)

templates = Jinja2Templates(directory="C:/Users/kawam/Desktop/html practice/homework/homework_week4/")

login_data = {
    "username": "test",
    "password": "test"
}

class ErrorType(str):
    empty_message="Please enter username and password",
    wrong_message="Username orpassword is not correct"

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    #return RedirectResponse(url="/signin")
    return templates.TemplateResponse("signin.html", {"request": request})

@app.post("/signin", response_class=HTMLResponse)
async def login(request: Request,username: Optional[str] = Form(None), password: Optional[str] = Form(None) ,remember_me: Optional[bool] = Form(None)):
    if username == login_data["username"] and password == login_data["password"] and remember_me:
        request.session["logged_in"] = True
        return RedirectResponse(url="/member")
    elif not username or not password:
        error_message = "帳號、或密碼不能為空"  # 自定義錯誤訊息
        return RedirectResponse(url=f"/error?message={error_message}")
    elif username != login_data["username"] or password != login_data["password"]:
        error_message = "帳號、或密碼輸入錯誤"  # 自定義錯誤訊息
        return RedirectResponse(url=f"/error?message={error_message}")

    '''
    elif username != login_data["username"] or password != login_data["password"]:
        
    elif remember_me is None or remember_me != 'on':
        error_message = "Please comfirm user manual"
        return RedirectResponse(url=f"/error?message={error_message}")'''
    
@app.post("/member", response_class=HTMLResponse)  
async def login_success(request: Request):
    print("Session:", request.session)
    if request.session.get("logged_in") == True:
        return templates.TemplateResponse("login_sucess.html", {"request": request})
    else:
        return templates.TemplateResponse("signin.html", {"request": request})

@app.post("/error", response_class=HTMLResponse)  
async def login_fail(request: Request):
    error_message = request.query_params.get("message")
    print("error_message=", error_message)
    return templates.TemplateResponse("login_fail.html", {"request": request, "message": error_message})


@app.get("/signout", response_class=HTMLResponse)
async def logout(request: Request):
    # 删除session数据
    request.session["logged_in"] = False
    print("Session:", request.session)
    return RedirectResponse(url="/")

'''
@app.get("/get-by-name")
def get_by_name(name:Optional[str]=None):#沒有default message，就算只輸入http://127.0.0.1:8000/get-by-name也不會返回fail
    for item_id in kittys:
        if kittys[item_id]['name']==name:#http://127.0.0.1:8000/get-by-name?name=Saipakhoo
            return kittys[item_id]
    raise HTTPException(status_code=404, detail='Item name not found')
'''
'''
@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})'''