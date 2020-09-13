#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :33.py
@说明    :Define a function which can print a dictionary where the keys are numbers between 1 and 3 
        (both included) and the values are square of keys.
@时间    :2020/09/02 15:44:28
@作者    :martin-ghs
@版本    :1.0
'''


def print_dict_fromOneToThree():
    my_dict = dict()
    for i in range(1, 4):
        my_dict[i] = i**2

    print(my_dict)


def main():
    print_dict_fromOneToThree()


if __name__ == "__main__":
    main()
