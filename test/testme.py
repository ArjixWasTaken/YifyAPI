from YifyAPI import yify as api
response = api.search_yify('avengers: endgame')[0]
print(response['title'], response['year'], response['qualities']['720p']['size'], response['qualities']['720p']['magnet'])
