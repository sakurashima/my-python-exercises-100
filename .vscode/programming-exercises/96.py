#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :96.py
@说明    :Please write a program which count and print the numbers of each character in a string input 
        by console.
        Example: If the following string is given as input to the program:

        abcdefgabc

        Then, the output of the program should be:

        a,2 c,2 b,2 e,1 d,1 g,1 f,1
@时间    :2020/09/11 16:51:15
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    count_dict = dict()
    input_message = input()

    for character in input_message:
        count_dict[character] = 0

    for character in input_message:
        count_dict[character] += 1

    for (i, x) in count_dict.items():
        print("%s:%d" % (i, x), end=" ")


if __name__ == '__main__':
    main()
