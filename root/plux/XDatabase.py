#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 1:47
# @Author  : cap669
# @File    : XDatabase.py
# @Software: PyCharm
from playhouse.pool import PooledPostgresqlDatabase
def DatabaseInject(name,host, port,user, password,max_connections,cheack:bool=True):
    def back(cls):
        cls.name = name
        cls.host = host
        cls.port = port
        cls.user = user
        cls.password = password
        cls.max_connections=max_connections
        cls.cheack = cheack
        return cls

    return back


class XDatabase:
    name:str
    host: str
    port: str
    user:str
    password: str
    max_connections:int
    cheack:bool
    def __init__(self):
        self.database = PooledPostgresqlDatabase(
            self.name,
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            max_connections=self.max_connections
        )
        if self.cheack:
            self.database.connect()
