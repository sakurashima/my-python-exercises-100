#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :57.py
@说明    :Define a custom exception class which takes a string message as attribute.
@时间    :2020/09/06 10:37:12
@作者    :martin-ghs
@版本    :1.0
'''


class StringError(object):
    def __init__(self, strs):
        self.waring = strs

    def raise_error(self):
        return self.waring


def main():
    mystr = "hello world"
    try:
        print(mystr[20])
    except:
        error = StringError("字符串索引超出范围")
        print(error.raise_error())

if __name__ == "__main__":
    main()
