#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :84.py
@说明    :Please write a program to shuffle and print the list [3,6,7,8].
@时间    :2020/09/09 16:46:40
@作者    :martin-ghs
@版本    :1.0
'''
from random import shuffle

def main():

    li = [3,6,7,8]
    shuffle(li)
    print(li)

if __name__ == '__main__':
    main()