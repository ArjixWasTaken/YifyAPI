This is my API for scraping (Yify)[https://yts.mx]

**#USAGE**

First you have to import it.

```python
from YifyAPI import yify
```

Now you are ready to use it!

Currently the only method is :

```python 
search_yify(query: str)
```

It will return a list with dictionaries for each movie result found, example below:

```
{
 'title': 'Sonic the Hedgehog', 
 'year': '2020', 
 'link': 'https://yts.mx/movies/sonic-the-hedgehog-2020', 
 'image': 'https://img.yts.mx/assets/images/movies/sonic_the_hedgehog_2020/medium-cover.jpg', 
 'qualities': {
     '720p': {
         'size': '908.03 MB', 
         'magnet': 'magnet:?.....'}, 
     '1080p': {
         'size': '1.82 GB', 
         'magnet': 'magnet:?.....'}
 }
}
```

if something goes bad and there was an error then it will return this:

```json
{'status': "error"}
```

So make sure to check if the response is equal to the one above with an if statement.



If you encounter any bug with my code or you want to contribute in any way then [here](https://github.com/arjixgamer/) is the github link
