#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :69.py
@说明    :Please write a program using generator to print the numbers which can be divisible by 5 and 7 

between 0 and n in comma separated form while n is input by console.

Example: If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70

@时间    :2020/09/08 16:06:36
@作者    :martin-ghs
@版本    :1.0
'''


def num_generator(n):
    i = 0
    while i <= n:
        if i % 5 == 0 and i % 7 == 0:
            yield i
        i += 1


def main():

    target_num_list = list()
    for num in num_generator(int(input("enter a num: "))):
        target_num_list.append(str(num))

    print(",".join(target_num_list))


if __name__ == "__main__":
    main()
