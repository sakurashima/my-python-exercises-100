#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :48.py
@说明    :Write a program which can filter() to make a list whose elements are even number between 1 and
         20 (both included).
@时间    :2020/09/06 08:49:37
@作者    :martin-ghs
@版本    :1.0
'''


def main():
    li = list()
    for i in range(1, 21):
        li.append(i)

    li = filter(lambda x: x % 2 == 0, li)
    print(list(li))

    # evenNumbers = filter(lambda x: x%2==0, range(1,21))
    # print(evenNumbers)


if __name__ == "__main__":
    main()
