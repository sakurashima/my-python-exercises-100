#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :83.py
@说明    :Please write a program to print the running time of execution of "1+1" for 100 times.
@时间    :2020/09/09 16:30:35
@作者    :martin-ghs
@版本    :1.0
'''
import time


def main():

    s_time = time.time()
    for i in range(100):
        1+1
    f_time = time.time()
    print(f_time-s_time)


if __name__ == '__main__':
    main()
