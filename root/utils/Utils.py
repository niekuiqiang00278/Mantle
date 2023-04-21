#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/22 0:07
# @Author  : cap669
# @File    : Utils.py
# @Software: PyCharm
import datetime
from uuid import uuid4


class Utils:
    @classmethod
    def u0(cls):
        return datetime.datetime.now()

    @classmethod
    def u1(cls):
        return cls.u0().replace(microsecond=0)

    @classmethod
    def u2(cls):
        return cls.u0().__str__()

    @classmethod
    def u3(cls):
        return cls.u1().__str__()

    @classmethod
    def f0(cls):
        return uuid4()

    @classmethod
    def f1(cls):
        return cls.f0().__str__()

    @classmethod
    def f2(cls):
        return cls.f0().hex

# Tips     :
