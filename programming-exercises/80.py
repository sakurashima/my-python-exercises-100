#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :80.py
@说明    :Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 
        7 , between 1 and 1000 inclusive.
@时间    :2020/09/08 16:47:17
@作者    :martin-ghs
@版本    :1.0
'''
import random


def main():

    ret = random.sample([x for x in range(1, 1001) if x % 5 == 0 and x % 7 == 0], 5)
    print(ret)


if __name__ == '__main__':
    main()
