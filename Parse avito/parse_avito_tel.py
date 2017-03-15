# -*- coding: utf8 -*-
from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string


class bot:
    def __init__(self):
        ch_path = r"C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
        self.driver = webdriver.Chrome(ch_path)
        self.navigate()

    def tel_recognaze(self):
        image = Image.open('tel.gif')
        print(image_to_string(image))

    def take_screen(self):
        self.driver.save_screenshot('avitoscreen.png')
    def crop(self, location, size):
        x= location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        print(x,y, width, height)

        x1 = x+width
        y1 = y - height
        image = Image.open('avitoscreen.png')
        image.crop((x, y, x1, y1)).save('tel.gif')

        self.tel_recognaze()


    def navigate(self):
        self.driver.get('https://kaspi.kz/')
        # button = self.driver.find_elements_by_xpath('//button[@class=""]')
        # button.click()
        sleep(5)
        self.take_screen()


        image = self.driver.find_element_by_xpath('//*[@id="headerRegionSelection"]')
        location = image.location # dict {x: 5896, y : 421}
        size = image.size          # dict {hight 500, width : 300}

        self.crop(location, size)




def main():
    b = bot()

if __name__ == '__main__':
    main()

