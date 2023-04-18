#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 2:14
# @Author  : cap669
# @File    : Cur.py
# @Software: PyCharm
# from abc import ABC,ABCMeta,abstractmethod
from data.config.TestDBConfig import testdbconf
from root.plux.XDatabase import XDatabase, DatabaseInject


@DatabaseInject(name='lln',host=testdbconf.host, port=testdbconf.port,user=testdbconf.user, password=testdbconf.password)
class TestDb(XDatabase):
    pass

database = TestDb().database
