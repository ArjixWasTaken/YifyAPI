import requests, json
from bs4 import BeautifulSoup

def get_html(url, proxy=None):
	if not proxy:
		return BeautifulSoup(requests.get(url).text, 'html.parser')
	else:
		proxy = {proxy.split(':')[0]: proxy}
		return BeautifulSoup(requests.get(url, proxies=proxy).text, 'html.parser')

def search_yify(query: str, proxy=None):
	results_list = []
	url = f'https://yts.mx/ajax/search?query={query}'
	if not proxy:
		response = requests.get(url).json()
	else:
		proxy = {proxy.split(':')[0]: proxy}
		response = requests.get(url, proxies=proxy).json()
	try:
		for movie in response['data']:
			try:
				html = get_html(movie['url'])
				soup = html.find_all('a', class_='avatar-thumb')
				crew = [[x.img['alt'].replace('Picture', '').strip(), x['href']] for x in soup]
				_720p = html.find('div', id='modal-quality-720p')
				try:
					_1080p = html.find('div', id='modal-quality-1080p')
				except:
					pass
				_720p_size = _720p.find_next('p', class_="quality-size").find_next('p', class_="quality-size").text
				try:
					_1080p_size = _1080p.find_next('p', class_="quality-size").find_next('p', class_="quality-size").text
				except:
					_1080p_size = 'N/A'
				_720p_magnet = _720p.find_next('a', class_="magnet-download download-torrent magnet")['href']
				try:
					_1080p_magnet = _1080p.find_next('a', class_="magnet-download download-torrent magnet")['href']
				except:
					_1080p_magnet = 'N/A'
				entry = \
				{
					"title": movie['title'],
					"year": movie['year'],
					"director": crew.pop(0),
					"cast": crew,
					"subtitles": 'https://yifysubtitles.org/movie-imdb/' + html.find('a', title='IMDb Rating')['href'].split('title/')[-1],
					"related_movies": [[x['title'], x['href']] for x in html.find('div', id='movie-related').find_all('a')],
					"synopsis": html.select('#synopsis > p.hidden-sm.hidden-md.hidden-lg')[0].text.strip(),
					"categories": [x.strip() for x in html.select("#movie-info > div.hidden-xs > h2:nth-child(3)")[0].text.split('/')],
					"link": movie['url'],
					'imdbLink': html.find('a', title='IMDb Rating')['href'],
					"trailer": ["N/A" if "https://www.youtube.com/watch?v=" + html.find('a', id='playTrailer')['href'].split('?')[0].split('/')[-1].strip() == "https://www.youtube.com/watch?v=" else "https://www.youtube.com/watch?v=" + html.find('a', id='playTrailer')['href'].split('?')[0].split('/')[-1].strip()][0],
					"imdbRating": html.find('span', itemprop='ratingValue').text + '/10',
					"image": {
						"small": movie['img'],
						"large": html.find('img', class_='img-responsive')['src']
					},
					"qualities":{ x.find('span').text + '.' + x.find('p', class_='quality-size').text: {
				"size": x.find('p', class_='quality-size').find_next('p', class_='quality-size').text, 
				"magnet": x.find('a', class_="magnet-download download-torrent magnet")['href']}
				for x in html.find_all('div', class_='modal-torrent')}
				}
				results_list.append(entry)
			except:
				continue


	except:
		results_list = {'status': "error"}
	return results_list