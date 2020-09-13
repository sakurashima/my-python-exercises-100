#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :65.py
@说明    :Write a program to compute:

f(n)=f(n-1)+100 when n>0 and f(0)=1

with a given n input by console (n>0).

Example: If the following n is given as input to the program:

5

Then, the output of the program should be:

500
@时间    :2020/09/07 15:02:41
@作者    :martin-ghs
@版本    :1.0
'''


def recursion(num):

    
    if num == 0:
        sum = 0
    else:    
        sum = recursion(num-1)+100
    return sum


def main():

    sum = recursion(int(input("Enter a num: ")))
    print("sum=%d" % sum)


if __name__ == "__main__":
    main()
