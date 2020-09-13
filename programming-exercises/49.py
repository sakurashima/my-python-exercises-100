#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :49.py
@说明    :Write a program which can map() to make a list whose elements are square of numbers between 1 
        and 20 (both included).
@时间    :2020/09/06 08:53:01
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    li = map(lambda x: x**2, list(filter(lambda x: x % 2 == 0, range(1, 21))))
    print(list(li))


if __name__ == "__main__":
    main()
