#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :70.py
@说明    :Please write assert statements to verify that every number in the list [2,4,6,8] is even.
@时间    :2020/09/08 16:10:34
@作者    :martin-ghs
@版本    :1.0
'''
def main():


    li = [2, 4, 6, 8]
    for i in li:
        assert i % 2 == 0


if __name__ == "__main__":
    main()
