#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :30.py
@说明    :Define a function that can accept two strings as input and concatenate them and then print it 
         in console.
@时间    :2020/09/02 15:30:25
@作者    :martin-ghs
@版本    :1.0
'''


def concat_strings(str1, str2):
    print(str1 + str2)


def main():
    concat_strings("Use + to ", "concatenate the strings")

if __name__ == "__main__":
    main()
