from aiohttp import web

from src.parsers.pochta.main import MailParser

routes = web.RouteTableDef()


@routes.get('/pochta')
async def pochta(request):
    from_city = request.rel_url.query['from_city']
    from_street = request.rel_url.query['from_street']
    to_city = request.rel_url.query['to_city']
    to_street = request.rel_url.query['to_street']
    cost = MailParser.get_price(from_city, from_street, to_city, to_street)
    return web.json_response(cost)
# /pochta?from_city=москва&from_street=алтуфьевское&to_city=уфа&to_street=парковая

@routes.get('/echo')
async def hello(request):
    data = {
        'Example': 'Echo Request'
    }
    return web.json_response(data)


app = web.Application()
app.add_routes(routes)
web.run_app(app)
