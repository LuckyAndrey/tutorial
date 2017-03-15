# -*- coding: utf8 -*-
import PIL.ImageGrab
import datetime

d1 = datetime.datetime.now().strftime('%Y-%M-%D %H%M%S')
print(d1)
print(type(d1))
img = PIL.ImageGrab.grab()
img.save(str(str(d1[:4])+'.png'), 'png')





def main():
    print(d1)



if __name__ == '__main__':
    main()