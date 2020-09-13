#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :53.py
@说明    :Define a class named Rectangle which can be constructed by a length and width. The Rectangle 
        class has a method which can compute the area.
@时间    :2020/09/06 09:17:47
@作者    :martin-ghs
@版本    :1.0
'''


class Rectangle(object):

    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def area(self):

        return self.length*self.width


def main():

    arectangle = Rectangle(10, 10)
    print(arectangle.area())


if __name__ == "__main__":
    main()
