#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 19:40
# @Author  : cap669
# @File    : UecWrapper.py
# @Software: PyCharm
# from abc import ABC,ABCMeta,abstractmethod
from root.plux.XWrapper import XWrapper
from root.utils.StateUtils import StateUtils


class UecWrapper(XWrapper):
    def sync_function(self, func, *args, **kwargs):
        state = StateUtils()
        return func(*args, **kwargs, state=state)

