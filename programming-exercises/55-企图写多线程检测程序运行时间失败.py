#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :55.py
@说明    :Please raise a RuntimeError exception.
@时间    :2020/09/06 10:01:06
@作者    :martin-ghs
@版本    :1.0
'''
import time
import threading


def func():
    for i in range(1, 5):
        print(i)
        time.sleep(1)


def compute_time():
    print("d")
    time.sleep(1)


def main():

    # print("{:.2f}".format(function_time))
    # if function_time > 4:
    #     raise("RuntimeError")
    # t1 = threading.Thread(target=compute_time)
    # t2 = threading.Thread(target=func)
    # t1.start()
    # t2.start()
    raise RuntimeError("something was wrong") #抛出错误


if __name__ == "__main__":
    main()
