import requests
from bs4 import BeautifulSoup

job_title = input('Enter the job title: ')
res = requests.get(f'https://merojob.com/search/?q={job_title}')
soup = BeautifulSoup(res.text,'html.parser')

jobs = soup.find_all('div' ,class_ = 'card mt-3 hover-shadow')
with open('job.txt', 'w') as f:
    if jobs:
        for job in jobs:
            f.write('Job title: ' +job.find('h1').find('a').text.strip() + '    ')
            f.write('Company name: '+ job.find('h3').find('a').text.strip() + '    ')
            if job.find('span', class_='text-muted') is not None:
                f.write('Company location: '+ job.find('span', class_='text-muted').text.strip() + '    ')
            else:
                f.write('Location not found       ')    
            f.write('link ' + 'https://merojob.com' + job.find('h1').find('a').get('href') + '\n')
    else:
        f.write('Job not found')
    #itemprop='addressLocality'
#page1 = soup.find_all('')
#for item in page:
#    address.append(page.find('span', itemprop='addressLocality').text)