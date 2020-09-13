#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :94.py
@说明    :With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list 
        after removing all duplicate values with original order reserved.
@时间    :2020/09/11 16:44:11
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    set1 = set([12,24,35,24,88,120,155,88,120,155])
    print(sorted(set1))

if __name__ == '__main__':
    main()