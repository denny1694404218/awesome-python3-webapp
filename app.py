import logging:logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

async def index(request):
    
    return web.Response(text='<h1>Index</h1>')



async def hello(request):
    
    text = '<h1>hello,s!</h1>'
    return web.Response(text=text)

async def init():
    app = web.Application()
    app.add_routes([web.get('/',index),
                    web.get('/hello',hello)])
    
    print('Server started at http://127.0.0.1:8000...')
    return app

web.run_app(init())
