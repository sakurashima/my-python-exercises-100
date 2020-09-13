#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :90.py
@说明    :By using list comprehension, please write a program generate a 358 3D array whose each element 
        is 0.
@时间    :2020/09/11 16:31:04
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    # array = [[0 for i in range(8)] for col in range(5)] for row in range(3)]
    array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]

    print(array)


if __name__ == '__main__':
    main()
