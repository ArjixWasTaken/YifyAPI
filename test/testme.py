from YifyAPI import yify as api
from ProxyFinder import get_proxy as gp
proxy = gp()
response = api.search_yify('avengers: endgame', proxy=proxy)[0]
result = [response['title'], response['year'], response['qualities']['720p']['size'], response['qualities']['720p']['magnet']]
print(result)