#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :75.py
@说明    :Please generate a random float where the value is between 5 and 95 using Python math module.
@时间    :2020/09/08 16:35:23
@作者    :martin-ghs
@版本    :1.0
'''
import random

def main():

    print(random.random()*100-5)
    

if __name__ == '__main__':
    main()
