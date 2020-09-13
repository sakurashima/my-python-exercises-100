#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :54.py
@说明    :Define a class named Shape and its subclass Square. The Square class has an init function 
        which takes a length as argument. Both classes have a area function which can print the area 
        of the shape where Shape's area is 0 by default.
@时间    :2020/09/06 09:55:37
@作者    :martin-ghs
@版本    :1.0
'''


class Shape(object):

    def __init__(self):
        pass

    def area(self):
        return self.area


class Square(Shape):
    def __init__(self, l=None):
        if not l:
            self.area = 0
        else:
            self.length = l


def main():
    mysquare = Square()
    print(mysquare.area)


if __name__ == "__main__":
    main()
