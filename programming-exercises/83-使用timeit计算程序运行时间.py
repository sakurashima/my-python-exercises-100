#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :83-使用timeit计算程序运行时间.py
@说明    :
@时间    :2020/09/09 16:39:40
@作者    :martin-ghs
@版本    :1.0
'''
from timeit import Timer

def main():

    t = Timer("for i in range(10): 1+1")
    print(t.timeit())
    print(t.repeat(1))





if __name__ == '__main__':
    main()