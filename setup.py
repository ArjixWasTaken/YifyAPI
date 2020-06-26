#!/usr/bin/env python3

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()



setup(
    name = 'YifyAPI',
    version = '0.0.5',
    author = 'ArjixGamer',
    author_email = 'arjixg53@gmail.com',
    description = 'Download your favourite movies',
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
