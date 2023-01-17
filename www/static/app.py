# -*- coding: utf-8 -*-

from aiohttp import web

async def awesome(request):
    text = 'awesome'
    return web.Response(text=text, content_type='text/html', charset='utf-8')

routes = list()
routes.append(web.get('/', awesome))
app = web.Application()
app.add_routes(routes)

host = '127.0.0.1'
port = 9000
web.run_app(app, host=host, port=port)