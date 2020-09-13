#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :51.py
@说明    :Define a class named American and its subclass NewYorker.
@时间    :2020/09/06 09:00:33
@作者    :martin-ghs
@版本    :1.0
'''


class American(object):
    pass


class NewYorker(American):
    pass


def main():

    anAmerican = American()

    aNewYorker = NewYorker()
    print(anAmerican)
    print(aNewYorker)


if __name__ == "__main__":
    main()
