from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

kittys={
    1:{
        'name':'Saipakhoo',
        'age':'2y9m',
        'color':'black'
    },
    2:{
        'name':"Hooia",
        'age':'2y',
        'color':'tabby'
    },
    3:{
        'name':"Hoekimkoo",
        'age':'1y2m',
        'color':'orange'
    }
}

@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

@app.get("/get-item/{item_id}")
def get_item(item_id:int = Path(description='The ID of kittys',gt=0,lt=10)):
    #在/docs/目錄中輸入使用者的提示詞
    #gt=greater than,lt=less than，設定item id長度範圍
    return kittys[item_id]
#http://127.0.0.1:8000/get-item/1

@app.get("/get-by-name")
def get_by_name(name:Optional[str]=None):#沒有default message，就算只輸入http://127.0.0.1:8000/get-by-name也不會返回fail
    for item_id in kittys:
        if kittys[item_id]['name']==name:#http://127.0.0.1:8000/get-by-name?name=Saipakhoo
            return kittys[item_id]
    raise HTTPException(status_code=404, detail='Item name not found')

@app.get("/file")
def file():
    return {"Hello": "This is new file"}

class Item(BaseModel):
    name:str
    age:str
    color:Optional[str]=None

@app.post("/create-item/{item_id}")
def create_item(item_id:int,item:Item):
    if item_id in kittys:
        raise HTTPException(status_code=400, detail='Item already exists.')
    kittys[item_id]={'name':item.name,'age':item.age,'color':item.color}
    return kittys[item_id]

class Update_Item(BaseModel):
    name:Optional[str]=None
    age:Optional[str]=None
    color:Optional[str]=None

@app.put("/update-item/{item_id}")
def update_item(item_id:int,item:Update_Item):
    if item_id not in kittys:
        raise HTTPException(status_code=404, detail='Item not exists.')
    if item.name!=None:
        kittys[item_id]['name']=item.name
    if item.age!=None:
        kittys[item_id]['age']=item.age
    if item.color!=None:
        kittys[item_id]['color']=item.color
    return kittys[item_id]

@app.delete("/delete-item/{item_id}")
def delete_item(item_id:int = Path(...,description='The ID of the item to delete.',gt=0,lt=10)):
    if item_id not in kittys:
        raise HTTPException(status_code=404, detail='Item not exists.')
    
    del kittys[item_id]
#uvicorn try_fastAPI:app --reload
#--reload: make the server restart after code changes. Only use for development.
#/docs
#/redoc