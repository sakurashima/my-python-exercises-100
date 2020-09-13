#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :25.py
@说明    :Question: Define a class, which have a class parameter and have a same instance parameter.
@时间    :2020/09/02 15:04:03
@作者    :martin-ghs
@版本    :1.0
'''


class MyClass(object):

    name = "Person"

    def __init__(self, name=None):
        self.name = name


def main():

    print(MyClass.name)  # 类属性可以不经过实例化就在外部进行调用
    new = MyClass("John")
    print(new.name) 


if __name__ == "__main__":
    main()
