def get_version():
	import feedparser
	r = feedparser.parse('https://pypi.org/rss/project/yifyapi/releases.xml')['entries'][0]['title']
	f = feedparser.parse('https://pypi.org/rss/project/yifyapi/releases.xml')['entries'][0]['title']
	l = int(r.split('.')[-1]) + 1
	__version__ = f.split('.')
	__version__ = __version__[0] + '.' + __version__[1] + '.' + str(l)
	return __version__