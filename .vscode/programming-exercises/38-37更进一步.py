#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :38.py
@说明    :Define a function which can generate a list where the values are square of numbers between 1 
         and 20 (both included). Then the function needs to print the first 5 elements in the list.
@时间    :2020/09/02 16:18:03
@作者    :martin-ghs
@版本    :1.0
'''
def generate_list_from1To20():

    num_list = list()

    for i in range(1, 21):
        num_list.append(i**2)

    # for i in range(0, 5):
    #     print(num_list[i])
    print(num_list[:5])


def main():
    generate_list_from1To20()


if __name__ == "__main__":
    main()

