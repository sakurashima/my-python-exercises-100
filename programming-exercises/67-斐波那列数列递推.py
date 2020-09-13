#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :67.py
@说明    :The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example: If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13
@时间    :2020/09/07 15:57:18
@作者    :martin-ghs
@版本    :1.0
'''


def recusion_Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recusion_Fibonacci(n-2) + recusion_Fibonacci(n-1)


def main():

    Fabonacci_list = list()

    for i in range(0, int(input("enter a num:"))+1):
        Fabonacci_list.append(str(recusion_Fibonacci(i)))
        
    print(Fabonacci_list)
    print(",".join(Fabonacci_list))


if __name__ == "__main__":
    main()
