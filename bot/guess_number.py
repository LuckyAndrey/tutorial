from random import randint as r
i=0
# your_number = input('Введите ваш вариант: ')
# number = r(10,15)
# print(number)
# while (i < 5):
#     your_number = input('Введите ваш вариант: ')
#     if int(your_number) == number:
#         print("You win")
#         break
#     else:
#         print('your lost')
#     i+=1

x = [1,2,3,4,5,6,7,8]
x.append(100)
x.insert(0,300)
x.pop(0)
# x.clear()
y = x.copy()
y.remove(100)
z= y.count(y)
print(x)
print(y[:5])
print(z)

import csv

with open('export.csv', encoding='utf-8') as scv_file:
    readscv = csv.reader(scv_file, delimiter =';')
    a=[]
    b=[]
    c=[]
    d =[]
    for row in readscv:
        a.append(row[1])
        b.append(row[2])
        c.append(row[4])
        d.append(row[4])
for v in a:
    print(v)
