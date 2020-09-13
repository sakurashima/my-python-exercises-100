#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :96-综合运用字典多种方法.py
@说明    :
@时间    :2020/09/13 08:17:21
@作者    :martin-ghs
@版本    :1.0
'''


def main():

    dic = {}
    s = input()
    for s in s:
        dic[s] = dic.get(s, 0)+1
    print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))


if __name__ == '__main__':
    main()
