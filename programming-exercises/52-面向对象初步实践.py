#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :52.py
@说明    :Define a class named Circle which can be constructed by a radius. The Circle class has a method
         which can compute the area.
@时间    :2020/09/06 09:03:05
@作者    :martin-ghs
@版本    :1.0
'''


class Circle():

    PI = 3.14

    def __init__(self, radius):

        self.radius = radius

    def compute(self):

        print("半径是{}的圆的面积是{:.2f}".format(self.radius, Circle.PI**2*self.radius))


def main():
    acircle = Circle(10)
    acircle.compute()


if __name__ == "__main__":
    main()
