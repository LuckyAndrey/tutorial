# coding=utf-8
import json
from random import choice
import faker
import threading

def gen_data():
    d = faker.Faker()
    # print(d.get_providers())
    person = {}

    name = d.name()
    # print(type(name))
    # name = name.decode('utf-8')
    tel = d.phone_number()
    # tel = d.misc()
        # print(name, tel)
    person ={name:tel}
        # person ={'name':name,                 'tel':tel}
        # print(person)
    return person

def write_json(dict_data):
    try:
        data = json.load(open('list.json', 'r'))
    except:
        data = []
    data.append(dict_data)
    with open('list.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)



json_list = []

def main():
    print("now ")
    for i in range(50):
        # print(json_list)
        write_json(gen_data())

threads = []
for i in range(5):
    t = threading.Thread(target=main, args=(i,))
    threads.append(t)
    t.start()
    #     json_list.append(gen_data())
    # with open('list.json', 'w') as f:
    #   json.dump(json_list, f, indent=2, ensure_ascii=True)#, ensure_ascii=True

if __name__=='__main__':
    main()