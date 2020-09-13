#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :45.py
@说明    :Write a program which can filter even numbers in a list by using filter function. The list is: 
         [1,2,3,4,5,6,7,8,9,10].
@时间    :2020/09/02 16:36:14
@作者    :martin-ghs
@版本    :1.0
'''


def filter_numslist(num):

    return num % 2 == 0


def main():

    wild_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    ret_list = list(filter(filter_numslist, wild_list))
    print(ret_list)


if __name__ == "__main__":
    main()
