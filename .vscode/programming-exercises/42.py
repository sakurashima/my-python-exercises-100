#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :42.py
@说明    :With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in 
         one line and the last half values in one line.
@时间    :2020/09/02 16:25:26
@作者    :martin-ghs
@版本    :1.0
'''
def main():

    given_tuple = (1,2,3,4,5,6,7,8,9,10)
    print(given_tuple[:5])
    print(given_tuple[5:])

if __name__ == "__main__":
    main()

