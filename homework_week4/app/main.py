from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse,RedirectResponse,JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(SessionMiddleware, secret_key = 'test', https_only = True)

templates = Jinja2Templates(directory="templates")

login_data = {
    "username": "test",
    "password": "test"
}

class ErrorType(str):
    empty_message="Please enter username and password",
    wrong_message="Username or password is not correct"

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    #return RedirectResponse(url="/signin")
    return templates.TemplateResponse("signin.html", {"request": request})

@app.post("/signin", response_class=HTMLResponse)
async def login(request: Request,username: Optional[str] = Form(None), password: Optional[str] = Form(None) ,remember_me: Optional[bool] = Form(None)):
    if username == login_data["username"] and password == login_data["password"] and remember_me:
        request.session["logged_in"] = True
        request.session.pop("error_message", None)
        print("Session:", request.session)
        #return RedirectResponse(url="/member")
        #return request.session["logged_in"] == True
        # return JSONResponse(content={"error": error_message})
        return JSONResponse(content={"login": request.session})
    elif not username or not password:
        error_message = "Please enter username and password"  # 自定義錯誤訊息
        request.session["error_message"] = error_message
        #request.session["logged_in"] = False
        return JSONResponse(content={"error": error_message})
    elif username != login_data["username"] or password != login_data["password"]:
        error_message = "Username or password is not correct"  # 自定義錯誤訊息
        request.session["error_message"] = error_message
        #request.session["logged_in"] = False
        return JSONResponse(content={"error": error_message})
    
@app.get("/member", response_class=HTMLResponse)  
async def login_success(request: Request):
    print("Session:", request.session)
    if request.session.get("logged_in") == True:
    #if request.session["logged_in"] == True:
        #清除緩存，讓登入頁面不要被存取，避免按上一頁就可以返回/member
        response = templates.TemplateResponse("login_sucess.html", {"request": request})
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0" 
        return response
    #if request.session.get("logged_in") == False:
    else:
        return RedirectResponse(url="/")
    #else:
        #return templates.TemplateResponse("signin.html", {"request": request})

@app.get("/error_dealing", response_class=HTMLResponse)  
async def login_fail(request: Request):
    error_message = request.session.get("error_message")  
    return RedirectResponse(url=f"/error?message={error_message}")

@app.get("/error", response_class=HTMLResponse)  
async def login_fail(request: Request):
    error_message = request.session.get("error_message")
    #print("error_message=", error_message)
    
    return templates.TemplateResponse("login_fail.html", {"request": request, "message": error_message})
    


@app.get("/signout", response_class=HTMLResponse)
async def logout(request: Request):
    # 删除session数据
    request.session["logged_in"] = False
    #request.session.pop("logged_in", None)
    #request.session.clear()
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