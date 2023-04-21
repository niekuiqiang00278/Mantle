#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 2:14
# @Author  : cap669
# @File    : Cur.py
# @Software: PyCharm
from root.config.PsqlConfig import psqlconf
from root.plux.XDatabase import XDatabase, DatabaseInject
@DatabaseInject(name='jan',host=psqlconf.host, port=psqlconf.port,user=psqlconf.user, password=psqlconf.password,max_connections=psqlconf.max_connections)
class TestDb(XDatabase):
    pass

janbase = TestDb().database
