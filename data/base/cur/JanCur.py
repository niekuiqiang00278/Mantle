#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 23:53
# @Author  : cap669
# @File    : JanCur.py
# @Software: PyCharm
from data.base.Cur import janbase
from root.base.Cur import Job1Cur, Job0Cur, Job2Cur



class Jan0Cur(Job0Cur):
    class Meta:
        database = janbase
        table_name = 'jan0'


class Jan1Cur(Job1Cur):
    class Meta:
        database = janbase
        table_name = 'jan1'


class Jan2Cur(Job2Cur):
    class Meta:
        database = janbase
        table_name = 'jan2'
# Tips     :
