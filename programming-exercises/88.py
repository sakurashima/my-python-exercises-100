#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :88.py
@说明    :By using list comprehension, please write a program to print the list after removing delete 
        numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
@时间    :2020/09/11 16:23:48
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    li = [12, 24, 35, 70, 88, 120, 155]
    li = [x for x in li if x % 5 != 0 and x % 7 != 0]
    print(li)


if __name__ == '__main__':
    main()
