#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :31.py
@说明    :Define a function that can accept two strings as input and print the string with maximum length 
in console. If two strings have the same length, then the function should print al l strings line by line.
@时间    :2020/09/02 15:34:47
@作者    :martin-ghs
@版本    :1.0
'''
def print_maxlength_strs(str1, str2):

    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)
    else:
        print(str1)
        print(str2)


def main():

    print_maxlength_strs(input(), input())

if __name__ == "__main__":
    main()
