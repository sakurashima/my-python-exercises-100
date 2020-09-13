#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :50.py
@说明    :Define a class named American which has a static method called printNationality.
@时间    :2020/09/06 08:57:12
@作者    :martin-ghs
@版本    :1.0
'''


class American(object):

    @staticmethod
    def printNationality():
        print("Make The American Great Again!")


def main():

    american = American()
    american.printNationality()
    American.printNationality()



if __name__ == "__main__":
    main()
