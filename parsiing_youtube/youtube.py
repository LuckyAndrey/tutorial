# -*- coding: utf8 -*-

import requests
from bs4 import BeautifulSoup
import httplib2
import time
import pafy



# URL = 'https://www.youtube.com/playlist?list=PLUY1lsOTtPeJNBuSweXS9pcSKbP4mr32S' # link to playlist
# save_to = "E:\PYTHON\SELENIUM\DevNami"
URL = 'https://www.youtube.com/playlist?list=PLfAlku7WMht4Vm6ewLgdP9Ou8SCk4Zhar' # link to playlist
save_to = 'E:\PYTHON\TKinter'


def dounload(link, n, total):
    print('грузим')

    ss = pafy.new(link).getbest()
    info = pafy.new(link)
    print(info)
    try:
        filename = ss.download(filepath=save_to)
        print(' Downloaded {} from {}'.format(n,total),filename)
    except Exception as e:
        print (e.message, e.args)
        print(' cann`t download')
    # print(s.resolution, s.extension, s.get_filesize(), s.url)

def load_picture(link):
    h = httplib2.Http('.cache')
    response, content = h.request(link)
    out = open('img.jpg', 'wb')
    out.write(content)
    out.close()

def get_html(url):
    r = requests.get(url)
    return r.text

def parsing(html):
    links = []
    soup = BeautifulSoup(html, 'lxml')
    spisok = soup.find('tbody').find_all('tr', class_='pl-video yt-uix-tile ')
    for items in spisok:
        item = items.find('td', class_='pl-video-title').find('a').get('href')
        title = items.find('td', class_='pl-video-title').find('a').text
        # num = items.find('td', class_='pl-video-title').find('a').text.split('.')[0]
        # num = int(num)
        # if num > 21:
        links.append([title, 'https://www.youtube.com'+item])
    return title, links

def main():
    all_links = parsing(get_html(URL))
    print(all_links[1][:])

    total = len(all_links[1])
    for n, i in enumerate(all_links[1], 1):
        # print(i[1])
        dounload(i[1], n, total)

if __name__ == '__main__':
    main()
# dounload('https://www.youtube.com/watch?v=ocwEgRG8EIM&index=3&list=PLUY1lsOTtPeJNBuSweXS9pcSKbP4mr32S')