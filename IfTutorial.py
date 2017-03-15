import math
import urllib.request
from bs4 import BeautifulSoup
""""
def IfPH (ph):
    if ph == 5.0:
        print("Coffe")
    elif ph != 5:
        print("Error")

x = float(input("Enter; "))
print(IfPH(x))
"""
x = int(input("Enter"))
print(" You enter; ", x)
while (5<x):
    print("NOW: ",x)
    x = x-11

names = globals()['__builtins__'].__dict__.keys()
builtins = sorted([name for name in names if not name.startswith('_')])
print(builtins)

