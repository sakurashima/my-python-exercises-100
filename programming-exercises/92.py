#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :92.py
@说明    :By using list comprehension, please write a program to print the list after removing the value 
        24 in [12,24,35,24,88,120,155].
@时间    :2020/09/11 16:36:09
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    li = [12, 24, 35, 24, 88, 120, 155]
    li = [x for x in li if x != 24]
    print(li)


if __name__ == '__main__':
    main()
