#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/11 11:03
# @Author  : cap669
# @File    : PsqlConfig.py
# @Software: PyCharm
from pydantic import BaseSettings
from functools import lru_cache
from Config import env
class PSqlConfig(BaseSettings):
    host: str = '127.0.0.1'
    port: int =5432
    user:str='postgres'
    password: str
    max_connections:int = 8
class DevPSqlConfig(PSqlConfig):
    host = '192.168.31.123'
    port = 12009
    password = 'ccwsd789'
class ProPSqlConfig(PSqlConfig):
    host = ''

    port = 0
    password = ''


@lru_cache()
def register_config() -> PSqlConfig:
    return dict(
        dev=DevPSqlConfig,
        por=ProPSqlConfig,
    )[env]()


psqlconf = register_config()

