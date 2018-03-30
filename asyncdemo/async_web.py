#coding:utf_8


import asyncio
import logging
logging.basicConfig(level=logging.INFO)

from aiohttp import web


async def index(request):
    await  asyncio.sleep(0.5)
    r = web.Response(body=b'<h1>body</h1>')
    r.content_type = 'application/octet-stream'
    return r


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>'%request.match_info['name']
    r = web.Response(body=text.encode('utf_8'))
    # r.content_type = 'application/octet-stream'
    r.content_type = 'text/html;charset=utf-8'
    return r


async def init(loop):

    app = web.Application(loop=loop)
    app.router.add_route('GET','/', index)
    app.router.add_route('GET','/hello/{name}', hello)
    srv =  await loop.create_server(app.make_handler(), '127.0.0.1',9090)
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()



