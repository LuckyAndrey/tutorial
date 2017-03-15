import faker
import xlwt
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ch_path = r"C:\Program Files (x86)\Google\Chrome\chromedriver.exe"

br = webdriver.Chrome(ch_path)
br.get('http://google.com')
search=br.find_element_by_id('lst-ib')

search.send_keys('Python3')
search.send_keys(Keys.RETURN)


data = faker.Faker('ru_RU')


# wb = xlwt.Workbook()
# ws = wb.add_sheet('Example')
# for i in range(1,60000):
#     ws.write(i,0,data.name())
#     ws.write(i,2,data.city())
#     ws.write(i,3,data.email())
# wb.save('E:/tutorial/Parse avito/test2.xls')

stack = []
for i in range(1, 5):
    a = data.name().split()
    if len(a)>3:
        continue
    else:
        stack.append(a[0])
        # print(a[1])
print(Counter(stack))
def main():
    pass

if __name__ == '__main__':
    main()

