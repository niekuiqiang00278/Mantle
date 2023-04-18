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
    host: str
    port: int
    password: str
    minsize: int = 10
    maxsize: int = 10
    encoding:str="utf-8"
    decode_responses:bool = True

class DevPSqlConfig(PSqlConfig):
    host = ''
    port = 0
    password = ''
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

