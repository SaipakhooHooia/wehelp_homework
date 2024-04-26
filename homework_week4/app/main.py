from fastapi import FastAPI, Request, Form,Query, Path
from fastapi.responses import HTMLResponse,RedirectResponse,JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional,Union
from starlette.middleware.sessions import SessionMiddleware

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
    #return RedirectResponse(url="/signin")
    return templates.TemplateResponse("signin.html", {"request": request})

@app.post("/signin", response_class=HTMLResponse)
async def login(request: Request,username: Optional[str] = Form(None), password: Optional[str] = Form(None) ,remember_me: Optional[bool] = Form(None),message: Union[str, None] = Query(default=None, max_length=50)):
    if username == login_data["username"] and password == login_data["password"] and remember_me:
        request.session["logged_in"] = True
        print("Session:", request.session)
        return RedirectResponse(url="/member", status_code=303)#使用status code 303可以讓瀏覽器重新發一個get request
#async def login_fail(request: Request,username: Optional[str] = Form(None), password: Optional[str] = Form(None) ,remember_me: Optional[bool] = Form(None),message: Union[str, None] = Query(default=None, max_length=50)):
    elif not username or not password:
        error_message = "Please enter username and password"  # 自定義錯誤訊息
        return RedirectResponse(url=f"/error?message={error_message}", status_code=303)
    elif username != login_data["username"] or password != login_data["password"]:
        error_message = "Username or password is not correct"  # 自定義錯誤訊息
        #request.session["logged_in"] = False
        return RedirectResponse(url=f"/error?message={error_message}", status_code=303)
        #return RedirectResponse(url="/error?message=帳號，或密碼錯誤", status_code=303)
    
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
    #request.session.pop("logged_in", None)
    #request.session.clear()
    print("Session:", request.session)
    return RedirectResponse(url="/")

@app.get("/square/{positive}", response_class=HTMLResponse)
async def calcaulate(request: Request,positive: int = Path(...)):
    result = positive * positive
    return templates.TemplateResponse("calculate_result.html", {"request": request, "message": result})