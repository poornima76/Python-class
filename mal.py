import requests
from bs4 import BeautifulSoup
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'}
res = requests.get('https://myanimelist.net/') 
#headers = headers)
print(res.status_code)