#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :76.py
@说明    :Please write a program to output a random even number between 0 and 10 inclusive using random 
        module and list comprehension.
@时间    :2020/09/08 16:36:37
@作者    :martin-ghs
@版本    :1.0
'''
import random


def main():

    print(random.choice([i for i in range(11) if i % 2 == 0]))


if __name__ == '__main__':
    main()
