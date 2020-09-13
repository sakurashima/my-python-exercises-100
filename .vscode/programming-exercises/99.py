#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :99.py
@说明    :Please write a program which prints all permutations of [1,2,3]
@时间    :2020/09/13 08:27:15
@作者    :martin-ghs
@版本    :1.0
'''
from itertools import permutations
import numpy as np


def main():

    for i in permutations([1, 2, 3]):
        print(i)

    print(numpy.random.permutation([1, 2, 3]))


if __name__ == '__main__':
    main()
