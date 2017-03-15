nums = [1,2,3,4,5,6,7,8,9,10]
print(nums)
my_list = []

for n in nums:
    my_list.append(n*n)
print(my_list)

my_list1 = [n*n for n in nums]
print(my_list1)

my_list2 = []

my_list2 = [map(lambda n: n*n,  nums)]
print((my_list2))

my_list2 = []
for n in nums:
    if n%2 == 0:
        my_list2.append(n)
print(my_list2)

my_list = [filter(lambda n: n%2 == 0, nums)]
print(' Lambda ',my_list)
# ---------------------------------------------------
pairs = []
for letter in 'abcd':
    for i in range(1,3):
        pairs.append((letter,i))
print("pairs", pairs)

pairs = [(l, n) for l in 'abcd' for n in range(1,3)]
print(pairs)
# -----------------------------------------------
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(zip((names, heros)))
mu_disc ={}
for name, hero in zip(names, heros):
    mu_disc[name] = hero
print(mu_disc)
mu_disc = {name: hero for name, hero in zip(names, heros) if name == 'Peter'}
print(mu_disc)
# ----------------------------------------------------------

num = (1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,11,10)
my_set = {n for n in num if n > 5}
# for n in num:
#     my_set.add(n)
print(my_set)

# ----------------------------------------------------------

def gen_func(num):
    for i in num:
        yield i*i

my_gen = gen_func(my_set)
my_gen2 = (n*n for n in my_set)
for i in my_gen:
    print(i)
for i in my_gen2:
    print(i)


# ----------- sorted---------------------------------

li = [3,9,5,1,7,0,4,2]
sorted_li = sorted(li, reverse=True)
print(' Original:\t',li)
print(' Sorted:\t',sorted_li)

li.sort()
print(' Sort():\t',li)
#         --------------------------------------------
tup = (1,9,2,8,3,7,4,6,5)
s_tup = sorted(tup)
print('sort() tup:\t', s_tup)
# ----------------------------------------------

dic= {'name': 'Corey', 'job': 'programming', 'age': 'none', 'os': 'Mac'}
s_dic = sorted(dic)
print('sorted dictionary:\t', s_dic)
# -------------------------------------------

abcval = [-1,2,-5,6,5,0,7,-3,9]
s_abcval = sorted(abcval, key=abs)
print('no sort :\t',abcval)
print('sort absolute value:\t',s_abcval)
