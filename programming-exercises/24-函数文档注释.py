"""
Python has many built-in functions, and if you do not know how to use it, you can read document online or 
find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), 
raw_input()

And add document for your own function Hints: The built-in document method is doc

"""


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :24.py
@说明    :
@时间    :2020/09/01 17:20:59
@作者    :martin-ghs
@版本    :1.0
'''
print(int.__doc__)  # 函数说明文档
print(__file__)     # 当前文件路径
print(__name__)     # 调用函数名称


def square(num):
    """Return the square value of the num.
    """
    return num**2


def main():

    square(int(input("enter the num: ")))
    print(square.__doc__)   # 打印函数文档


if __name__ == "__main__":
    main()