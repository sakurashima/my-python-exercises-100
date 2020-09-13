#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :56.py
@说明    :Write a function to compute 5/0 and use try/except to catch the exceptions.
@时间    :2020/09/06 10:32:53
@作者    :martin-ghs
@版本    :1.0
'''

def main():
    try:
        ret = 5/0
    except ZeroDivisionError:
        print("零不能作除数")

if __name__ == "__main__":
    main()
