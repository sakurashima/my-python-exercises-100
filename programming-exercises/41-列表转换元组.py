#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :41.py
@说明    :Define a function which can generate and print a tuple where the value are square of numbers 
         between 1 and 20 (both included).
@时间    :2020/09/02 16:23:59
@作者    :martin-ghs
@版本    :1.0
'''


def printTuple():
    li = list()
    for i in range(1, 21):
        li.append(i**2)
    print(tuple(li))


printTuple()
