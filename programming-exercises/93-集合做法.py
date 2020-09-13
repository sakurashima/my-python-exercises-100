#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :93-集合做法.py
@说明    :With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a 
        list whose elements are intersection of the above given lists.
@时间    :2020/09/11 16:40:34
@作者    :martin-ghs
@版本    :1.0
'''


def main():


    set1 = set([1, 3, 6, 78, 35, 55])
    set2 = set([12, 24, 35, 24, 88, 120, 155])
    set_ = set1&set2
    li = list(set_)
    print(li)


if __name__ == '__main__':
    main()
