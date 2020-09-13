#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :79.py
@说明    :Please write a program to randomly generate a list with 5 even numbers between 100 and 200 
        inclusive.
@时间    :2020/09/08 16:45:17
@作者    :martin-ghs
@版本    :1.0
'''
import random


def main():

    ret = random.sample([x for x in range(100, 201) if x % 2 == 0], 5)
    print(ret)


if __name__ == '__main__':
    main()
