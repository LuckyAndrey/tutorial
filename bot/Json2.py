import requests
from bs4 import BeautifulSoup as bs
url ='https://geo.craigslist.org/iso/us'
headers = {'user-agent':'iphone'}
response = requests.get(url, headers = headers)
# print(response.status_code)
# print(response.headers)
# print(response.content)
soup = bs(response.content,'html.parser')
# print(soup.prettify())
city = soup.find('ul',{'class':'height6'})
city_dict = {}
for city in soup.find_all('a'):
    city_dict[city.text] = city['href']
# for k in sorted(city_dict.keys()):
#     print(k, city_dict[k])
sf_area = city_dict['SF bay area']
print(sf_area)
full_url = 'http:'+sf_area+'search/sss'
search_params = {'min_price':'300',
                 'query':'Apple iPhone 6'}
r = requests.get(full_url, params=search_params, headers=headers)
s = bs(r.content, 'html.parser')
# print(s.prettify())
price_list = []
for i, a in enumerate(s.find_all('a', {'class':'i gallery'})):
    price = a.find('span', {'class':'price'}).text
    if i<95:
        price_list.append(int(price[1:]))
print(price_list)

