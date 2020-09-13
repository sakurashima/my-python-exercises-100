#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :95.py
@说明    :Define a class Person and its two child classes: Male and Female. All classes have a method 
        "getGender" which can print "Male" for Male class and "Female" for Female class.
@时间    :2020/09/11 16:46:25
@作者    :martin-ghs
@版本    :1.0
'''


class Person(object):

    def getGender(self, gender=None):
        return Unknown


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):

    def getGender(self):
        return "female"


def main():

    boy = Male()
    print(boy.getGender())
    girl = Female()
    print(girl.getGender())


if __name__ == '__main__':
    main()
