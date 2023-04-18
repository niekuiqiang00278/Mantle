#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 2:08
# @Author  : cap669
# @File    : TestDBConfig.py
# @Software: PyCharm

from pydantic import BaseSettings
from functools import lru_cache
from Config import env
class TestDBConfig(BaseSettings):
    host: str = '127.0.0.1'
    port: int
    user:str= 'postgres'
    password: str

class DevTestDBConfig(TestDBConfig):
    host = ''
    port = 0
    password = ''

class ProTestDBConfig(TestDBConfig):
    host = ''
    port = 0
    password = ''


@lru_cache()
def register_config() -> TestDBConfig:
    return dict(
        dev=DevTestDBConfig,
        por=ProTestDBConfig,
    )[env]()


testdbconf = register_config()

