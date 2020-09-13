#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :60.py
@说明    :Write a program which accepts a sequence of words separated by whitespace as input to print the 

words composed of digits only.

Example: If the following words is given as input to the program:

2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

In case of input data being supplied to the question, it should be assumed to be a console input.
@时间    :2020/09/06 10:52:05
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    ret_li = list()

    strs_li = input("Enter the message: ").split(" ")
    for i in strs_li:
        if i.isdigit():
            ret_li.append(i)

    print(ret_li)
    # a = "3"
    # ret = a.isdigit()
    # print()

if __name__ == "__main__":
    main()
