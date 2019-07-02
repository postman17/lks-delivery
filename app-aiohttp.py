from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/echo')
async def hello(request):
    data = {
        'Example': 'Echo Request'
    }
    return web.json_response(data)


app = web.Application()
app.add_routes(routes)
web.run_app(app)
