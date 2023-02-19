# rating, name reviews, company type

import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'}
res = requests.get('https://www.ambitionbox.com/list-of-companies', headers = headers)

soup = BeautifulSoup(res.text, 'html.parser')
# print(res.status_code)
#403 Forbidden, the URl is okay but access is denied, server thinks we are a bot
# so we use the user agent, we can find this by clicking on inspect<network<headers<user-agent
company = soup.find_all('div', class_='company-info-wrapper')
# print(company.text)
with open('ambition-box.txt', 'w') as f:
    for companies in company:
        f.write('Company name: ' + companies.find('a').find('h2').text.strip() + '\n')
        f.write('Number of reviews: '+ companies.find('div', class_='rating-wrapper').find('a').text.strip().split(' ')[0].replace('(', ' ').replace('k', ' ') + '\n') 
        f.write('Company ratings: '+ companies.find('div', class_='rating-wrapper').find('p').text.strip() + '\n')
        f.write('Company info: '+ companies.find('div', class_='company-basic-info').find('p', class_='infoEntity sbold-list-header').text.strip() + '\n') 
        f.write('Company age: ' + companies.find_all('p',class_= 'infoEntity sbold-list-header')[2].text.strip().split(' ')[0] + '\n')
        f.write('-'*50 + '\n') 