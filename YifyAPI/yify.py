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
				soup = html.select('a.avatar-thumb')
				crew = [[x.img['alt'].replace('Picture', '').strip(), x['href']] for x in soup]
				entry = \
				{
					"title": movie['title'],
					"year": movie['year'],
					"director": crew.pop(0),
					"cast": crew,
					"subtitles": 'https://yifysubtitles.org/movie-imdb/' + html.select_one('a[title=\'IMDb Rating\']')['href'].split('title/')[-1],
					"related_movies": [[x['title'], x['href']] for x in html.select_one('div#movie-related').select('a')],
					"synopsis": html.select_one('div#synopsis > p.hidden-sm.hidden-md.hidden-lg').text.strip(),
					"categories": [x.strip() for x in html.select_one("div.hidden-xs > h2:nth-child(3)").text.split('/')],
					"link": movie['url'],
					'imdbLink': html.find('a', title='IMDb Rating')['href'],
					"trailer": ["N/A" if "https://www.youtube.com/watch?v=" + html.select_one('a#playTrailer')['href'].split('?')[0].split('/')[-1].strip() == "https://www.youtube.com/watch?v=" else "https://www.youtube.com/watch?v=" + html.select_one('a#playTrailer')['href'].split('?')[0].split('/')[-1].strip()][0],
					"imdbRating": float(html.select_one('span[itemprop=\'ratingValue\']').text),
					"image": {
						"small": movie['img'],
						"large": html.select_one('img.img-responsive')['src']
					},
					"qualities":
					[[x.find('span').text + '.' + x.select_one('p.quality-size').text, 
					x.find('p', class_='quality-size').find_next('p', class_='quality-size').text,
					x.select_one('a.magnet-download.download-torrent.magnet')['href']] 
					for x in html.select('div.modal-torrent')]
				}
				results_list.append(entry)
			except:
				continue


	except:
		results_list = {'status': "error"}
	return results_list
