#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :68.py
@说明    :Please write a program using generator to print the even numbers between 0 and n in comma 

separated form while n is input by console.

Example: If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10
@时间    :2020/09/07 16:24:36
@作者    :martin-ghs
@版本    :1.0
'''


def even_num_generator(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1


def main():

    even_list = []

    for i in even_num_generator(int(input("enter a num: "))):
        even_list.append(str(i))

    print(",".join(even_list))


if __name__ == "__main__":
    main()
