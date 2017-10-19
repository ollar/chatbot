import aiml
import os
import aiohttp
import asyncio
from tel import request_path

async def set_hook():
    async with aiohttp.ClientSession() as session:
        async with session.post(request_path('setWebhook'), data={
            'url': 'https://bf0cf6a1.ngrok.io/telega',
        }) as resp:
            print(resp.status)
            print(await resp.text())


# k = aiml.Kernel()
# cwd = os.getcwd()

# for root, dirs, files in os.walk('data'):
#     for file in files:
#         _f = os.path.join(cwd, 'data', file)
#         k.learn(_f)

# while True:
#     print(k.respond(input("> ")))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_hook())
