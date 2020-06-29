import requests
from bs4 import BeautifulSoup as bs

soup = bs(requests.get('https://yts.mx/movies/trolls-world-tour-2020').text, 'html.parser')
# soup = soup.select("div[class*=tech-spec-info col-xs-20]")
sou = soup.find_all(
	'div', attrs={
					'class':
						 lambda e: e.startswith('tech-spec-info col-xs-20') 
						 if e else False
				})
qualities = {
		
			x.find('span').text + '.' + x.find('p', class_='quality-size').text: {
				"size": x.find('p', class_='quality-size').find_next('p', class_='quality-size').text, 
				"magnet": x.find('a', class_="magnet-download download-torrent magnet")['href']}
				 
			for x in soup.find_all('div', class_='modal-torrent')
			}
# print(soup)
# print(soup)
print(qualities)