from aiohttp import web

from app import pochta


async def test_work(aiohttp_client, loop):
    app = web.Application()
    app.router.add_get('/pochta', pochta)
    client = await aiohttp_client(app)
    resp = await client.get('/pochta?from_city=москва&from_street=алтуфьевское&to_city=уфа&to_street=парковая')
    assert resp.status == 200
    text = await resp.text()
    assert '{"pochta": 259.34}' == text


async def test_not_work(aiohttp_client, loop):
    app = web.Application()
    app.router.add_get('/pochta', pochta)
    client = await aiohttp_client(app)
    resp = await client.get('/pochta?from_city=москва&from_street=алтуфьевское&to_city=уфа')
    assert resp.status == 200
    text = await resp.text()
    assert '{"pochta": null}' == text