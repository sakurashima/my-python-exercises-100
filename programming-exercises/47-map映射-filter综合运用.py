#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :47.py
@说明    :Write a program which can map() and filter() to make a list whose elements are square 
        of even number in [1,2,3,4,5,6,7,8,9,10].
@时间    :2020/09/06 08:45:19
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, li))))


if __name__ == "__main__":
    main()
