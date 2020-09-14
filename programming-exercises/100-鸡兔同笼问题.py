#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :100.py
@说明    :Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among 
        the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
@时间    :2020/09/13 08:54:44
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    num = {}
    for i in range(36):  # chicken
        # for j in range(36-i):  # rabbit
        j = 35 - i
        if 2*i + 4*j == 94:

            # 字典的get方法
            num["chickens"] = num.get("chickens", i)
            num["rabbits"] = num.get("rabbits", j)

    for i, j in num.items():
        print("%s: %d" % (i, j))


if __name__ == '__main__':
    main()
