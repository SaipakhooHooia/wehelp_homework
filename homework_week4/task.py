from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="C:/Users/kawam/Desktop/html practice/homework/homework_week4/")

login_data = {
    "username": "test",
    "password": "test"
}

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    #return RedirectResponse(url="/signin")
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/signin")
async def login(username: str = Form(), password: str = Form() ,remember_me: Optional[bool] = Form(None)):
    if username == login_data["username"] and password == login_data["password"] and remember_me:
        return RedirectResponse(url="/member")
    elif username != login_data["username"] or password != login_data["password"]:
        error_message = "wrong username or password"  # 自定義錯誤訊息
        return RedirectResponse(url=f"/error?message={error_message}")

    '''
    elif username != login_data["username"] or password != login_data["password"]:
        
    elif remember_me is None or remember_me != 'on':
        error_message = "Please comfirm user manual"
        return RedirectResponse(url=f"/error?message={error_message}")'''
    
@app.post("/member", response_class=HTMLResponse)  
async def login_success(request: Request):
    return templates.TemplateResponse("login_sucess.html", {"request": request})

@app.post("/error", response_class=HTMLResponse)  
async def login_fail(request: Request,error_message:Optional[str]=None):
    return templates.TemplateResponse("login_fail.html", {"request": request, "message": error_message})

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