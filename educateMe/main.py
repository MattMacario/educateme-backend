import uvicorn as uvicorn
from fastapi import FastAPI, Request
from mangum import Mangum
import boto3
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
handler = Mangum(app)
rds_client = boto3.client('rds-data', region_name='us-west-1')
templates = Jinja2Templates(directory="templates")

# template routes
@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})

@app.get('/afterRegister', response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("afterRegister.html", {'request': request})

@app.get('/teacherRegister', response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("teacherRegister.html", {'request': request})

@app.get('/studentRegister', response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("studentRegister.html", {'request': request})

@app.get('/donorRegister', response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("donorRegister.html", {'request': request})

@app.get('/login', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {'request': request})

@app.get('/studentLogin', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("studentLogin.html", {'request': request})

@app.get('/teacherLogin', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("teacherLogin.html", {'request': request})

@app.get('/donorLogin', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("donorLogin.html", {'request': request})

@app.get('/studentHome', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("studentHome.html", {'request': request})

@app.get('/afterLogout', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("afterLogout.html", {'request': request})

@app.get('/teacherHome', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("teacherHome.html", {'request': request})

@app.get('/donorHome', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("donorHome.html", {'request': request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8082, reload=True)


