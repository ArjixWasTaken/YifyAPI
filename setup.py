#!/usr/bin/env python3

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()


def get_version():
    import feedparser
    r = feedparser.parse('https://pypi.org/rss/project/yifyapi/releases.xml')['entries'][0]['title']
    f = feedparser.parse('https://pypi.org/rss/project/yifyapi/releases.xml')['entries'][0]['title']
    if int(r.split('.')[-1]) == 10:
    	ff = int(r.split('.')[-2]) + 1
    	l = 0
    else:
    	ff = int(r.split('.')[-2])
    	l = int(r.split('.')[-1]) + 1
    
    __version__ = f.split('.')
    __version__ = __version__[0] + '.' + str(ff) + '.' + str(l)
    return __version__
version = get_version()

setup(
    name = 'YifyAPI',
    version = version,
    author = 'ArjixGamer',
    author_email = 'arjixg53@gmail.com',
    description = 'A scraping API for Yify.',
    packages = find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
    url = 'https://github.com/ArjixGamer/YifyAPI',
    keywords = ['movies', 'yify', 'torrents', 'download', 'hd'],
    install_requires = [
        'beautifulsoup4>=4.6.0',
        'requests>=2.18.4',
    ],
    extras_require = {},
    long_description = long_description,
    long_description_content_type = 'text/markdown'
)