#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :82.py
@说明    :Please write a program to compress and decompress the string "hello world!hello world!hello 
        world!hello world!".
@时间    :2020/09/09 16:25:43
@作者    :martin-ghs
@版本    :1.0
'''
import zlib

def main():

    s = b"hello world!hello world!hello world!hello world!"
    t = zlib.compress(s)
    print(t)
    t = zlib.decompress(t)
    print(t)


if __name__ == '__main__':
    main()
