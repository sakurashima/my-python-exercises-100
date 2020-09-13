#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :32.py
@说明    :Define a function that can accept an integer number as input and print the "It is an even number"
         if the number is even, otherwise print "It is an odd number".
@时间    :2020/09/02 15:40:30
@作者    :martin-ghs
@版本    :1.0
'''


def is_evenOrodd(num):

    if num % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")


def main():
    is_evenOrodd(int(input("enter a num: ")))

if __name__ == "__main__":
    main()
