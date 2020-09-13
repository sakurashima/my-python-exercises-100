#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :89.py
@说明    :By using list comprehension, please write a program to print the list after removing the 0th, 
        2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
@时间    :2020/09/11 16:25:05
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    li = [12, 24, 35, 70, 88, 120, 155]

    li = list(enumerate(li))

    # for i, j in li:
    #     print("i=%d j=%d " % (i, j))

    # print(li)
 
    li = [x for (i, x) in li if i%2!=0]
    print(li)


if __name__ == '__main__':
    main()
