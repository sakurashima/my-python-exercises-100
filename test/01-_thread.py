#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :01-thread.py
@说明    :
@时间    :2020/09/06 10:15:36
@作者    :martin-ghs
@版本    :1.0
'''
import _thread
import time

# 为线程定义一个函数


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


def main():

  # 创建两个线程
    try:
        _thread.start_new_thread(print_time, ("Thread-1", 2, ))  # 前一个参数函数名，后面是该函数的参数
        _thread.start_new_thread(print_time, ("Thread-2", 4, ))
    except:
        print("Error: 无法启动线程")

    while 1:
        pass


if __name__ == "__main__":
    main()
