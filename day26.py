# web scraping 
import requests
from bs4 import BeautifulSoup
res = requests.get('https://news.ycombinator.com/')
print(res.status_code)
print(type(res))
# beautiful soup allows to parse string into  html and provide methods to access this html.
# convert string format of html to html code is done by html.parser library (Document Object Model)
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.prettify())
# print(soup.find('a')) # find the first anchor of the page
# print(soup.find_all('a')) # finds all anchor and put in a list
# news = soup.find_all('span', class_ = 'titleline')

# with open('news.txt', 'w') as f:
#     for data in news:
#         f.write(data.text + '\n' + data.find('a').get('href') + '\n' + '\n')
