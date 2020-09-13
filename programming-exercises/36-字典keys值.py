#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :36.py
@说明    :Define a function which can generate a dictionary where the keys are numbers between 1 and 20 
        (both included) and the values are square of keys. The function should just print the keys only.
@时间    :2020/09/02 16:12:36
@作者    :martin-ghs
@版本    :1.0
'''

def generate_dict():

    nums_dict = dict()
    for i in range(1, 21):
        nums_dict[i] = i**2
    # print(nums_dict.values())
    for i, j in nums_dict.items():
        print("keys: %d" % i)

def main():
    generate_dict()


if __name__ == "__main__":
    main()
