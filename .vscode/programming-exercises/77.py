#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :77.py
@说明    :Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 
        10 inclusive using random module and list comprehension.
@时间    :2020/09/08 16:39:42
@作者    :martin-ghs
@版本    :1.0
'''
import random


def main():

    ret = random.choice([x for x in range(201) if x % 5 == 0 and x % 7 == 0])
    print(ret)


if __name__ == '__main__':
    main()
