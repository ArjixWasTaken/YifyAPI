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
			try:
				html = get_html(movie['url'])
				soup = html.find_all('a', class_='avatar-thumb')
				crew = [[x.img['alt'].replace('Picture', '').strip(), x['href']] for x in soup]
				_720p = html.find('div', id='modal-quality-720p')
				_1080p = html.find('div', id='modal-quality-1080p')
				_720p_size = _720p.find_next('p', class_="quality-size").find_next('p', class_="quality-size").text
				_1080p_size = _1080p.find_next('p', class_="quality-size").find_next('p', class_="quality-size").text
				_720p_magnet = _720p.find_next('a', class_="magnet-download download-torrent magnet")['href']
				_1080p_magnet = _1080p.find_next('a', class_="magnet-download download-torrent magnet")['href']
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
				continue


	except:
		results_list = {'status': "error"}
	return results_list