# -*- coding: utf8 -*-
from tkinter import Tk, StringVar, ttk
from tkinter import *
import time
import datetime
import math



root = Tk()
root.title('parsing')
root.geometry('1320x640+0+0')
canvas = Canvas(root, width=1040, height=640, bg="#002")
canvas.pack(side=RIGHT)
# root.configure(background = 'black')
for y in range(21): # линии сетки
    k = 50*y
    canvas.create_line(20+k, 620, 20+k, 20, width=1, fill='#191338')

for x in range(13):
    k = 50 * x
    canvas.create_line(20, 20+k, 1020, 20+k, width=1, fill='#191338')

canvas.create_line(20,20, 20, 620, width=1, arrow=FIRST, fill='yellow')# Y
canvas.create_line(10,320, 1020, 320, width=1, arrow=LAST, fill='red') # X

canvas.create_text(20, 10, text='300', fill='white')
canvas.create_text(20, 630, text='-300', fill='white')
canvas.create_text(10, 310, text='0', fill='white')
canvas.create_text(1030, 310, text='1000', fill='white')

lable_omega = Label(root, text=' frequency')
lable_omega.place(x=0, y=10)
lable_fi = Label(root, text=' смещение по Х')
lable_fi.place(x=0, y=30)
lable_Amp = Label(root, text=' Амплитуда')
lable_Amp.place(x=0, y=50)
lable_Y = Label(root, text=' Смещение по У')
lable_Y.place(x=0, y=70)




# ------------------------------------------------
omega = Entry(root)
omega.place(x=150, y=10)
fi = Entry(root)
fi.place(x=150, y=30)
amp = Entry(root)
amp.place(x=150, y=50)
smesh = Entry(root)
smesh.place(x=150, y=70)

# ----------------------------
def sinus(omega, fi, amp, smesh):
    global sin
    print('here1')
    sin = 0
    xy = []
    for x in range(1000):
        y = math.sin(x*omega)
        xy.append(x+fi)
        xy.append(y*amp+smesh)
    sin = canvas.create_line(xy, fill='blue')

def clean():
    print('here')
    canvas.delete(sin)

# -----------------------------------



but_calc = Button(root, text='Расчитать')
but_calc.bind('<Button-1>', lambda event: sinus(float(omega.get()),
                                                float(fi.get()),
                                                float(amp.get()),
                                                float(smesh.get())
                                                ))
but_calc.place(x=10, y=100)

but_clean =Button(root, text='Clean')
but_clean.bind('<Button-1>', lambda event: clean())
but_clean.place(x=10, y=130)

w = 0.0209 # иклическа частота
phi = 10 # смещение по х
A =  200 # амплитуда
dy = 310 #  смещение Y






# ------------------------------------------------------------
#------------------------------ Varaibles-----------------------------------------
day = StringVar
link = StringVar

# ---------------------------------- components-----------------------------------------

# day.set(time.strptime('%d/%m/%Y'))


root.mainloop()