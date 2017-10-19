from aiohttp import web, ClientSession
import aiml
import os
from tel import request_path


k = aiml.Kernel()
cwd = os.getcwd()

for root, dirs, files in os.walk('data'):
    for file in files:
        _f = os.path.join(cwd, 'data', file)
        k.learn(_f)


async def index(request):
    # query = request.query.get('q')
    # return web.Response(text=k.respond(query))
    return web.Response(text='asas')


class Telega(web.View):
    def __init__(self, request, *args):
        super().__init__(request)

    async def post(self):
        data = await self._request.json()

        # print(dict(data))

        response = k.respond(data['message']['text']) or 'don\'t know'

        async with ClientSession() as session:
            async with session.post(request_path('sendMessage'), data={
                'chat_id': data['message']['chat']['id'],
                'text': response
            }) as resp:
                print(resp.status)
                print(await resp.text())

        return web.Response(text='ok')
