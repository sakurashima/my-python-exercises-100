#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :66.py
@说明    :The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:

7

Then, the output of the program should be:

13
@时间    :2020/09/07 15:35:02
@作者    :martin-ghs
@版本    :1.0
'''


def recusion(n):

    if n == 1:
        sum = 1
    elif n == 0:
        sum = 0
    else:
        sum = recusion(n-1) + recusion(n-2)
    return sum


def main():

    sum = recusion(int(input("enter a num: ")))
    print("sum=%d" % sum)


if __name__ == "__main__":
    main()
