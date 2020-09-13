#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :93.py
@说明    :With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a 
        list whose elements are intersection of the above given lists.
@时间    :2020/09/11 16:38:14
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    li1 = [1,3,6,78,35,55]
    li2 = [12,24,35,24,88,120,155]
    li = [x for x in li1 if x in li2]
    print(li)


if __name__ == '__main__':
    main()