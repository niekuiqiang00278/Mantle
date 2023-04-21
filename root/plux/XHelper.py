#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/22 2:42
# @Author  : cap669
# @File    : XHelper.py
# @Software: PyCharm
# from abc import ABC,ABCMeta,abstractmethod
name_list = ['job', 'task']


class XHelper:
    def __init__(self, name):
        if name in name_list:
            pass
        else:
            raise
        self.name = name


# Tips     :
