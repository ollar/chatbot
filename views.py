from aiohttp import web
import aiml
import os


k = aiml.Kernel()
cwd = os.getcwd()

for root, dirs, files in os.walk('data'):
    for file in files:
        _f = os.path.join(cwd, 'data', file)
        k.learn(_f)


async def index(request):
    query = request.query.get('q')
    return web.Response(text=k.respond(query))
