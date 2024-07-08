# 网络

# 使用 requests 发送 HTTP 请求
# 先安装库:  pip3 install requests  

import requests
import json


# 直接抓取百度首页，并保存为文本 baidu.html
res = requests.get('https://www.baidu.com')
with open('baidu.html', 'wb') as file:
    file.write(res.content)

# 同步的 get 请求
# 获取金山词霸每日一句
res = requests.get('https://open.iciba.com/dsapi/')
if res.status_code == 200:
    data = res.json()
     # 使用 json.dumps() 格式化输出
    print(json.dumps(data, indent=4, ensure_ascii=False))
else:
    print(f'请求失败: {res.status_code}')


# 同步的 post 请求
# 获取东方财富 000001 股票的资讯(前5条)
url = 'https://np-seclist.eastmoney.com/sec/getQuoteNews'
headers = {            
    'Content-Type': 'application/json'
}
params = json.dumps({
    'appKey': 'dae6383a91bc5198b36ea0e41f1f3d6b',
    'client_version': '10.18.5',
    'client': 'sec_ios',
    'sortEnd': '',
    'pageSize': 5,
    'midCode': '0.000001',
    'req_trace': '1C6969747011433F831672E769496649',
    'biz': 'sec_quote_news'
}) 

res = requests.post(url,headers=headers,data=params)
if res.status_code==200:
    data = res.json()
    print(json.dumps(data, indent=4, ensure_ascii=False))
else:
    print(f'请求失败: {res.status_code}')


print('\naiohttp------------------------------------------------------\n')
# 使用 aiohttp 发送异步 HTTP 请求
# 先安装库: pip3 install aiohttp  
import aiohttp
import asyncio

# 异步的 get 请求, 获取金山词霸每日一句
async def fetchData():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://open.iciba.com/dsapi/') as response:
            data = await response.text()
            obj = json.loads(data)
            print(json.dumps(obj, indent=4, ensure_ascii=False))

asyncio.run(fetchData())

# 异步的 post 请求, 获取东方财富 000001 股票的资讯(前5条)
async def fetchNews():
    async with aiohttp.ClientSession() as session:
        async with session.post(url,headers=headers,data=params) as response:
            data = await response.text()
            obj = json.loads(data)
            print(json.dumps(obj, indent=4, ensure_ascii=False))

asyncio.run(fetchNews())



# 使用 aiohttp 创建 web 应用
# 运行程序后，访问 http://0.0.0.0:3000/xxx
from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "cxy")
    text = f"Hello, {name}!"
    return web.Response(text=text)

def create_app():
    app = web.Application()
    app.add_routes([
        web.get("/{name}",  handle),
    ])
    return app

app = create_app()
web.run_app(app, host="0.0.0.0", port=3000)