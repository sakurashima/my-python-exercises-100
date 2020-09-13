#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :98.py
@说明    :Please write a program which accepts a string from console and print the characters that have 

even indexes.

Example: If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld
@时间    :2020/09/13 08:25:45
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    mystr = "H1e2l3l4o5w6o7r8l9d"
    print(mystr[::2])

if __name__ == '__main__':
    main()