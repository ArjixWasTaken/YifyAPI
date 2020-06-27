from YifyAPI import yify as api
from ProxyFinder import get_proxy as gp
import time
proxy = gp()
response = api.search_yify('avengers: endgame', proxy=proxy)[0]
time.sleep(3)
result = [response['title'], response['year'], response['qualities']['720p']['size'], response['qualities']['720p']['magnet']]
print(result)
