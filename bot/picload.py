

import requests
import os

urls = ['https://r.mradx.net/pictures/E4/228C00.jpg',
        'https://r.mradx.net/pictures/4D/C1BEB8.jpg',
        ]


def get_file(urls):
    # print('1')
    r = requests.get(urls, stream=True)
    print(r)
    return r

def get_name(url):
    name = url.split('/')[-1]
    folder = name.split('.')[0]
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.abspath(folder)
    fullpath = path + '\\'+ name
    print(fullpath)
    return str(fullpath)

def save_file(name, file_obj):
    print('name '+name)
    with open(name, 'bw') as file:
        for chank in file_obj.iter_content(1024*10):
            file.write(chank)



for i in urls:
    save_file(get_name(i), get_file(i))
