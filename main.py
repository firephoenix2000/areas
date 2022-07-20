# -- coding: utf-8 --
# @Time : 7/8/22 11:35 PM
# @Author : yudejun
# @Email : yudejun2000@outlook.com
# @File : main.py
# @Software: PyCharm

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import random,gauss
from shape import Triangle,Point


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def generate_data():

    with open('data.txt', mode='a', encoding='utf-8') as datafile:

        for i in range(50):
            x1 = random()*10
            y1 = random()*10
            x2 = random()*10
            y2 = random()*10
            x3 = random()*10
            y3 = random()*10

            triangle = Triangle(Point(x1, y1), Point(x2, y2), Point(x3, y3))
            s = triangle.calc_area()
            gaussnumber = gauss(0,0.04)
            print('gaussnumber is :', gaussnumber)
            adjust_s = s * (1+ gaussnumber)
            print(s, adjust_s)
            # w_list = [x1,y1,x2,y2,x3,y3,adjust_s]
            writestr = x1,y1,x2,y2,x3,y3,adjust_s
            datafile.write(str(writestr)+'\n')

if __name__ == '__main__':
    # print_hi('PyCharm')
    generate_data()

