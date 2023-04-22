#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 23:10
# @Author  : cap669
# @File    : Cur.py
# @Software: PyCharm
# from abc import ABC,ABCMeta,abstractmethod
from root.config.PsqlConfig import psqlconf
from root.plux.XDatabase import DatabaseInject, XDatabase
from peewee import Model, TextField, BooleanField,DateTimeField,IntegerField
import datetime
q0 = datetime.datetime(1999,12,13,0,0,0,0000)

class Job0Cur(Model):
    uid = TextField(unique=True)
    # 唯一任务ID
    info = TextField()
    # 信息
    fnsh = IntegerField(default=1)
    # 1 原始任务 2 锁定任务 3 任务错误 4 任务成功
    msg = TextField(default='nuxx')
    # 消息
    ctime = DateTimeField()
    # 创建任务的时间
    rtime = DateTimeField(default=q0)
    # 最后一次访问时间
    stime = DateTimeField(default=q0)
    # 完成任务后的时间
    aka = TextField(default='nuxx')
    # 一占位符为索引


class Job1Cur(Job0Cur):
    an = IntegerField()
    # 任务总量
    en = IntegerField()
    # 任务累积量



class Job2Cur(Model):
    uid = TextField(unique=True)
    # 唯一任务ID
    info = TextField()
    # 信息
    msg = TextField(default='nuxx')
    # 消息
    ctime = DateTimeField()
    # 创建任务的时间
    rtime = DateTimeField(default=q0)
    # 最后一次访问时间
    stime = DateTimeField(default=q0)
    # 完成任务后的时间
    diff = IntegerField(default=-1)
    # 验证点
    aka = TextField(default='nuxx')
    # 一占位符为索引

@DatabaseInject(name='test', host=psqlconf.host, port=psqlconf.port,
                user=psqlconf.user, password=psqlconf.password,
                max_connections=psqlconf.max_connections)
class TestDb(XDatabase):
    pass


# testbase = TestDb().database
# Tips     :
