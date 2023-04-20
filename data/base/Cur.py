#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 2:14
# @Author  : cap669
# @File    : Cur.py
# @Software: PyCharm
from root.config.PsqlConfig import psqlconf
from root.plux.XDatabase import XDatabase, DatabaseInject
@DatabaseInject(name='lln',host=psqlconf.host, port=psqlconf.port,user=psqlconf.user, password=psqlconf.password)
class TestDb(XDatabase):
    pass

database = TestDb().database
