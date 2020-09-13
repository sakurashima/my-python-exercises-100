#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :58.py
@说明    :Assuming that we have some email addresses in the "username@companyname.com" format, please 
        write program to print the user name of a given email address. Both user names and company names 
        are composed of letters only.
@时间    :2020/09/06 10:43:25
@作者    :martin-ghs
@版本    :1.0
'''
import re


def main():

    email = input(
        "Enter the email addresses:  \n(format like this: username@companyname.com)\n")
    pattern = "(\w+)@(\w+).com"
    ret = re.search(pattern, email)
    if ret:
        username = ret.group(1)
        companyname = ret.group(2)
        print("username:{}\ncompanyname:{}".format(username, companyname))
    else:
        print("未提取到信息")


if __name__ == "__main__":
    main()
