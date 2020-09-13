#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :46.py
@说明    :Write a program which can map() to make a list whose elements are square of elements in 
        [1,2,3,4,5,6,7,8,9,10].
@时间    :2020/09/06 08:34:33
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    squaredNumbers = map(lambda x: x**2, li)
    print(list(squaredNumbers))

    

if __name__ == "__main__":
    main()
