dist: bionic
language: python

python:
  - "3.8"

cache: pip

install:
  - pip install feedparser
  - python setup.py install

script:
  - python ./test/testme.py
