#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :97.py
@说明    :Please write a program which accepts a string from console and print it in reverse order.

Example: If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir
@时间    :2020/09/13 08:18:51
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    input_message = "rise to vote sir"
    print(input_message[::-1])


if __name__ == '__main__':
    main()
