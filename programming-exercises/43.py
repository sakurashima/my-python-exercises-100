#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :43.py
@说明    :Write a program to generate and print another tuple whose values are even numbers in the given 
         tuple (1,2,3,4,5,6,7,8,9,10)
@时间    :2020/09/02 16:27:56
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    my_tuple = list()

    for i in given_tuple:
        if i % 2 == 0:
            my_tuple.append(i)
    print(tuple(my_tuple))


if __name__ == "__main__":
    main()
