#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :39.py
@说明    :Define a function which can generate a list where the values are square of numbers between 1 
         and 20 (both included). Then the function needs to print the last 5 elements in the list.
@时间    :2020/09/02 16:20:08
@作者    :martin-ghs
@版本    :1.0
'''
def generate_list_from1To20():

    num_list = list()

    for i in range(1, 21):
        num_list.append(i**2)

    print(num_list[-5:]) # 列表中倒数最后五个数字


def main():
    generate_list_from1To20()


if __name__ == "__main__":
    main()
