import asyncio
from proxybroker import Broker
import os

async def save(proxies, filename):
    """Save proxies to a file."""
    with open(filename, 'w') as f:
        while True:
            proxy = await proxies.get()
            if proxy is None:
                break
            proto = 'https' if 'HTTPS' in proxy.types else 'http'
            row = '%s://%s:%d\n' % (proto, proxy.host, proxy.port)
            f.write(row)


def get_proxy():
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(
        broker.grab(countries=['US', 'GB'], limit=1),
        save(proxies, filename='proxies.txt'),
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)
    with open('proxies.txt', 'r') as f:
    	proxy = f.read().replace('\n', '')
    os.remove('proxies.txt')
    return proxy