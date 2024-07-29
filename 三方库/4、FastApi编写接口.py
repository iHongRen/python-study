# FastApi 编写接口
# pip3 install fastapi

# 文档 https://fastapi.tiangolo.com/zh/

# FastAPI 是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python 并基于标准的 Python 类型提示。我们可以用它来编写服务端接口。

from fastapi import FastAPI,UploadFile,File,Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import time

# 创建 FastAPI 应用
app = FastAPI()

# 允许跨域 - 根据需求设置，这里使用*通配符，表示允许所有
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 自定义中间件 -- 计算处理时间，添加自定义响应头'X-Process-Time'
@app.middleware("http")
async def add_process_time_header(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# 中间件 - 添加自定义响应头'Access-Control-Allow-Private-Network'
@app.middleware("http")
async def add_other_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Private-Network"] = "true"
    return response


# GET请求，定义路由 / , 处理函数 root, 返回值为 {"message": "Hello World"}
# 访问地址：http://127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}



# GET 定义路由 /items/{item_id} & 定义路由处理函数, 接收一个可选的query参数 q
# 访问地址：http://127.0.0.1:8000/items/1?q=hello
# 返回：{"item_id": 1, "q": "hello"}
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    # 我们可以在这里编写更多的代码，比如从数据库中读取数据
    return {"item_id": item_id, "q": q}



# 服务程序运行后，会自动生成的交互式 API 文档, 可在文档里调试接口
# Swagger UI风格接口文档
# 访问地址：http://127.0.0.1:8000/docs


# 可选的 API 文档，Redoc
# 访问地址：http://127.0.0.1:8000/redoc


# FastAPI 使用定义 API 的 OpenAPI 标准将你的所有 API 转换成「模式」。
# 查看 openapi.json
# 访问地址：http://127.0.0.1:8000/openapi.json


# POST请求,上传文件并接收一个字符串参数
# 需要先安装 pip3 install python-multipart
# 使用交互文档来测试接口 http://127.0.0.1:8000/docs
# 选择POST /upload 这个接口，点击 "Try it out"，选择 "Upload File"，上传文件并输入字符串
# 或者使用 curl 命令，
# curl -X 'POST' \
#   'http://127.0.0.1:8000/upload' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: multipart/form-data' \
#   -F 'file=@/xxx/test.png' \
#   -F 'text=测试参数'
# 接口返回：
# {
#   "filename": "1024.png",
#   "size": 423448,
#   "text": "测试参数"
# }
@app.post("/upload")
async def upload(file: UploadFile = File(), text: str = Form()):
    # 读取文件内容
    contents = await file.read()

    # 保存文件到当前目录
    with open(file.filename, "wb") as f:
        f.write(contents)

    return {
        "filename": file.filename, 
        "size": len(contents), # 文件大小(字节数)
        "text": text
    }


# 用作静态文件服务器
# 访问地址：http://127.0.0.1:8000/static/index.html
app.mount("/static", StaticFiles(directory="static"), name="static")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# 终端运行本程序：
# $> uvicorn 4、FastApi编写接口:app --reload --host 0.0.0.0 --port 8000
# '4、FastApi编写接口' 是本程序的文件名
# 'app' 是 FastAPI 应用实例的变量名
# '--reload' 表示在修改代码后自动重启服务
# '--host 0.0.0.0' 表示监听所有可用的 IP 地址，这样任何能够与该机器通信的人都可以公开访问它
# '--port 8000' 表示服务端口为 8000
