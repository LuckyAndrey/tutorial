
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import re
import httplib2
import os

result = {}
path_for_images = os.getcwd()
print(path_for_images)

main_url = 'https://www.livelib.ru/genres'
def load_picture(link):
    h = httplib2.Http('.cache')
    response, content = h.request(link)
    out = open('img.jpg', 'wb')
    out.write(content)
    out.close()

def click_all():
    ch_path = r"C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
    driver = webdriver.Chrome(ch_path)
    driver.get('https://www.livelib.ru/genres')
    driver.find_element_by_xpath()



# --------------------------------
#  get list of categories
def get_html(url):
  r = requests.get(url)
  print(r.encoding)
  r = r.text.encode('utf-8')
  # print(r.encoding)
  return r
# ------------------------

# html = get_html(main_url)
html = open("list.html",'r', encoding='utf-8')
books_category = {}

def load_image(url, name):
    path = 'E:\tutorial\Parce_Lib\list_files\\'
    # name = re.findall(r'_.\w',url)
    h = httplib2.Http('.cache')
    name = url.split('._')[1]
    name = name
    response, content = h.request(url)
    out = open(path+name, 'wb')
    out.write(content)
    out.close()


def get_category(html):
    soup = bs(html, 'lxml')
    # soup = bs(html, 'html.parser')
    categories = soup.find('div', class_="column-670 subcontainer").find_all('div', class_="card-white genre-block")
    catalog = []

    for i in categories:
        # print(books_total_in_genre)
        main_genre_title = str(i.find_all('a', class_='main-genre-title')).split('">')[-1].split('</a>')[0]
        books_total_in_genre = (i.find('span', class_='genre-books-count').text)
        books_total_in_genre = books_total_in_genre.replace(' ','')
        sub_title2 = str(i.find_all('a', class_='main-genre-title')).split('href="')[-1].split('">')[0]
        catalog.append((main_genre_title, books_total_in_genre, sub_title2))
        # main_genre_title = i.get_text()
        result[main_genre_title] = None
        # print(result.keys())
    # print(len(catalog[1:]))

    return catalog[1:]



def books_parsing(catalog, dict):
    total_genre = len(catalog)
    check = total_genre-total_genre+1 # сколько парсим
    parsing_books_list = []
    for i in catalog:
        # parsing_books_list.append(i[2])
        # for i in range(0, (int(len(parsing_list))-int(len(parsing_list))+1)): # for request
        # url = get_html(parsing_list[i])
        url = open('business.html','r', encoding='utf-8')
        # print(url)
        soup = bs(url, 'lxml')
        books = soup.find('table', class_="list").find_all('tr', class_="column-670 subcontainer version4")
        main_genre_title = i[0]#str(i.find('a', class_='main-genre-title'))#.split('">')[-1].split('</a>')[0]
        # print(main_genre_title)
        for b in books:
            # print(type(b))
            # print('--------------------------------------------------------------------------------------------')
            book = b.find('td', class_='column-430').find('a').text
            link = b.find('a', class_='tag-book-title with-cycle').get('href')
            img_link = b.find('div', 'margin-bottom')
            img_name = str(b.find('div', class_='block').find_all('a')).split('src=".')[1].split('"')[0].split('_—_')[1]
            # img_link = str(b.find('div', class_='block').find('div').find_all('a'))#.split('src=".')[1].split('"')[0]
            # img = b.find('div', class_='block').find_all('a').split('src=".')[1].split('"')[0]
            parsing_books_list.append((book, link))
            dict['Книги по психологии'] = (book, link)
            # dict[main_genre_title] = (book, link)
            print(dict)

            # print(book, type(img_link))





books_parsing(get_category(open("list.html",'r', encoding='utf-8')), result)


numbers_categories = get_category(html)












# --------------------------
def main():
    # get_html(main_url)
    pass

if __name__ == 'main':
    main()