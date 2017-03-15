import csv

import requests
from bs4 import BeautifulSoup


url = "https://www.avito.ru/moskva/telefony?sgtd=1&q=htc"

#  quantity of pages
# form urls
# get data
def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_ = 'pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = int(pages.split('=')[1].split('&')[0])
    print(total_pages)
    return total_pages
# -------------------------------------------------------------




def write_header():
    with open('avita.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(('N','Название', 'Цена', 'Метро', 'ссылка'))

# ---------------------------------------------------------------


def writeCSV(data):

    with open('avita.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['index'],
                         data['title'],
                         data['price'],
                         data['metro'],
                         data['url']))
        # print(len(ads))

def get_data_html(html):
    index =0
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    for ad in ads:
        index += 1
        name = ad.find('div', class_='description').find('h3', class_="title item-description-title").text.strip().lower()
        if 'htc' in name:
            try:
                title = ad.find('div', class_='description').find('h3', class_="title item-description-title").text.strip()
                title = title.replace(',','')
                # title = ad.find('div', class_='description').find('h3', class_='title item-description-title').text.strip()
                # print('size ', len(title), title)
            except:
                title = ''
            try:
                price = ad.find('div', class_='description').find_all('div', class_='about')
                price = str(price).split('>')[1].split('<')[0].strip()
                # if 'M8 32Gb' in title:
                #     print(index, 'price=============================  ',price, 'len === ',len(price))
                # price = ad.find('div', class_='description').find('div', class_='about').text.strip()
            except:
               price = "Not price"
            try:
                metro = ad.find('div', class_='data').find_all('p')[1].text.split()[-1]
            except:
                metro = ""
            try:
                ur = 'https://www.avito.ru'+ad.find('div', class_='description').find('a').get('href')
                print(ur)
            except:
                ur = 'wwwwwww'
            data = {"index":index,
                'title': title,
                'price':price,
                'metro':metro,
                'url':ur}
            # print('data   ',data)
            writeCSV(data)
        else:
            continue


# print(title+ price+ metro+ur)
write_header()
total_page = get_total_pages(get_html(url))
for n, i in enumerate(range(1, 2)):
    base_url = 'https://www.avito.ru/moskva/telefony?p='
    query = '&q=htc'
    gen_url = base_url+str(i)+query
    # print(n,gen_url)
    html = get_html(gen_url)
    get_data_html(html)

print(get_total_pages(get_html(url)))


def main():
    pass

if __name__ == 'main':
    main()

# https://www.avito.ru/moskva/telefony?p=5&q=htc
# https://www.avito.ru/moskva/telefony?p=2&q=htc