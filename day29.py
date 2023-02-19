import requests
from bs4 import BeautifulSoup
quote_name = input('Enter the type of quotes you want to scrape: ')
res = requests.get(f'https://www.goodreads.com/quotes/tag/{quote_name}'  )
if res.status_code == 404:
    print('Enter the correct tag')
soup = BeautifulSoup(res.text, 'html.parser')

quote = soup.find_all('div',class_ = 'quoteText')

with open('qoutes.txt', 'w') as f:
    for i in quote:
        f.write(i.text.strip().split('―')[0].strip() + '\n')
        f.write('-' + i.text.strip().split('―')[1].strip()+ '\n') 

#i.find('span', class_='authorOrTitle').text.strip() + '\n'