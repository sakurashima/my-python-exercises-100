#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :02-threading模块.py
@说明    :threading模块
@时间    :2020/09/06 10:22:24
@作者    :martin-ghs
@版本    :1.0
'''
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


def main():


if __name__ == "__main__":
    main()
