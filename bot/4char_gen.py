import random

import time

char = ['A','B','Z','X','C','V','B','N','M','Q','W','R','T','P']
digits = [1,2,3,4,5,6,7,8,9]
file=[]
index_char = 0
for line in range(202): # количество строк
    char_Q = random.randint(0,4)
    digit_Q = 4-char_Q
    string =''
    for letter in range(0,1):
        liter =''
        digit = ''
        for a in range(0,char_Q):
            letter = char[random.randint(0,len(char)-1)]
            liter = liter + letter
        for d in range(0,digit_Q):
            digit += str(digits[random.randint(0,len(digits)-1)])
        string = (string +liter+digit)
    file.append(string)
    # print(string)
with open('Gen.txt', 'w') as f:
    for string in file:
        f.write(str(string)+'\n')

print(file)


def squares(nums):
    result = []
    for n in nums:
        result.append(n*n)
    return result
print(squares([1,2,3,4,5]))
mynums = [x*x for x in [1,2,3,4,5]]
print(mynums)