#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :86.py
@说明    :Please write a program to generate all sentences where subject is in ["I", "You"] and verb is 
        in ["Play", "Love"] and the object is in ["Hockey","Football"].
@时间    :2020/09/09 16:52:00
@作者    :martin-ghs
@版本    :1.0
'''
import random


def main():

    sub_li = ["I", "You"]
    verb_li = ["Play", "Love"]
    obj_li = ["Hockey", "Football"]

    for i in sub_li:
        for j in verb_li:
            for k in obj_li:
                print(i+" " + j + " " + k)


if __name__ == '__main__':
    main()
