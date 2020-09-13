#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :44.py
@说明    :Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" 
         or "Yes", otherwise print "No".
@时间    :2020/09/02 16:32:42
@作者    :martin-ghs
@版本    :1.0
'''


def main():
    strs = input()
    if strs in ["yes", "YES", "Yes"]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
