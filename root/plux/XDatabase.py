#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 1:47
# @Author  : cap669
# @File    : XDatabase.py
# @Software: PyCharm
from peewee import PostgresqlDatabase


def DatabaseInject(name,host, port,user, password):
    def back(cls):
        cls.name = name
        cls.host = host
        cls.port = port
        cls.user = user
        cls.password = password

        return cls

    return back


class XDatabase:
    name:str
    host: str
    port: str
    user:str
    password: str

    def __init__(self):
        self.database = PostgresqlDatabase(
            self.name,
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
        )
