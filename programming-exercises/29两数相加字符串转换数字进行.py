#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :29.py
@说明    :Define a function that can receive two integral numbers in string form and compute their sum 
         and then print it in console.
@时间    :2020/09/02 15:21:36
@作者    :martin-ghs
@版本    :1.0
'''


def num_two_str():

    nums_list = input("enter two integral num: ").split(" ")

    print(int(nums_list[0]) + int(nums_list[1])) 


def main():

    num_two_str()


if __name__ == "__main__":
    main()
