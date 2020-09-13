#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :91.py
@说明    :By using list comprehension, please write a program to print the list after removing the 0th,
        4th,5th numbers in [12,24,35,70,88,120,155].
@时间    :2020/09/11 16:34:42
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    li = [12, 24, 35, 70, 88, 120, 155]
    li = list(enumerate(li))

    li = [x for (i, x) in li if i not in [0, 4, 5]]
    print(li)


if __name__ == '__main__':
    main()
