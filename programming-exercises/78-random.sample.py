#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :78.py
@说明    :Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
@时间    :2020/09/08 16:41:49
@作者    :martin-ghs
@版本    :1.0
'''
import random


def main():
    print(random.sample(range(100), 5))


if __name__ == '__main__':
    main()
