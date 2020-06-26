import requests, json
from bs4 import BeautifulSoup

def get_html(url):
	return BeautifulSoup(requests.get(url).text, 'html.parser')

def search_yify(query: str):
	results_list = []
	url = f'https://yts.mx/ajax/search?query={query}'
	response = requests.get(url).json()
	try:
		for movie in response['data']:
			html = get_html(movie['url'])
			_720p = html.find('div', id='modal-quality-720p')
			_1080p = html.find('div', id='modal-quality-1080p')
			_720p_size = _720p.find_next('p', class_="quality-size").find_next('p', class_="quality-size").text
			_1080p_size = _1080p.find_next('p', class_="quality-size").find_next('p', class_="quality-size").text
			_720p_magnet = _720p.find_next('a', class_="magnet-download download-torrent magnet")['href']
			_1080p_magnet = _1080p.find_next('a', class_="magnet-download download-torrent magnet")['href']
			entry = {
				"title": movie['title'],
				"year": movie['year'],
				"link": movie['url'],
				"image": html.find('img', class_='img-responsive')['src'],
				"qualities":{
					"720p": {
						"size": _720p_size,
						"magnet": _720p_magnet
					},
					"1080p": {
						"size": _1080p_size,
						"magnet": _1080p_magnet
					}
				}}
			results_list.append(entry)


	except:
		results_list = {'status': "error"}
	return results_list