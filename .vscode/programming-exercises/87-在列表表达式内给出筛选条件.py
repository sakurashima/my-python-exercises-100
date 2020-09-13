#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :87.py
@说明    :Please write a program to print the list after removing delete even numbers in 
        [5,6,77,45,22,12,24].
@时间    :2020/09/11 16:21:55
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    li = [5, 6, 77, 45, 22, 12, 24]
    li = [x for x in li if x % 2 != 0]
    print(li)


if __name__ == '__main__':
    main()
