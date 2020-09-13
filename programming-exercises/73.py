#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :73.py
@说明    :Please write a binary search function which searches an item in a sorted list. The function 
        should return the index of element to be searched in the list.
@时间    :2020/09/08 16:25:48
@作者    :martin-ghs
@版本    :1.0
'''


def bin_search(li, target_num):

    index = -1
    cnt = 0
    for num in li:
        if num == target_num:
            index = cnt
            break
        cnt += 1

    return index


def main():

    li = [2, 5, 7, 9, 11, 17, 222]

    print(bin_search(li, 11))
    print(bin_search(li, 12))


if __name__ == "__main__":
    main()
