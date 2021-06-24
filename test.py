from os import name
import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.models import encode_multipart_formdata

url = "https://clutch.co/developers/artificial-intelligence"

print('req page')
response = requests.get(url)
print("got response", response.status_code)

data = response.text
soup = BeautifulSoup(data, 'html.parser')

## Scrapping Start

comp_total = {}
comp_no = 0

response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,'html.parser')
lists = soup.find_all('li',{'class':'provider provider-row sponsor'})

for list in lists:
    
    name = soup.find('ul',{'class':'directory-list active'}).find('h3',{'class': 'company_info'}).find('a').text
    rating = list.find('div', {'class': 'rating-reviews'}, {'data-content': 'Avg. hourly rate'}).find('span').text
    Project_size = list.find('div', {'class': 'list-item block_tag custom_popover'}, {'data-content': 'Min. project size'}).find('span').text
    Hourly_rate = list.find('div', {'class': 'list-item custom_popover'}, {'data-content': 'Avg. hourly rate'}).find('span').text
    employees = list.find('div',{'data-content': '<i>Employees</i>'}).find('span').text
    location = list.find('div',{'data-content': '<i>Location</i>'}).find('span', {'class': 'locality'}).text
    focus = list.find('div', {'class': 'carousel-item active'}).text

    comp_no+=1
    comp_total[comp_no] = [name, rating, Project_size, Hourly_rate, employees, location, focus]

    
url_tag = soup.find('a',{'class': 'page-link'}, {'data-page': ''})
if url_tag.get('href'):
    url= 'https://clutch.co/developers/artificial-intelligence' + '?' + 'page=' + url_tag.get('data-page')
else:
    print('End of page')


print("Total Companies:", comp_no)
comp_total_df = pd.DataFrame.from_dict(comp_total, orient = 'index', columns = ['Company Name','Rating','Project Size', 'Rates', 'No of Employees', 'Location', 'Focus Area'])
# print(comp_total_df)



comp_total_df.to_csv('comp_total.csv')
    
    
    
    
