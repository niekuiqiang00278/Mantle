#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/3 2:51
# @Author  : cap669
# @File    : RedConfig.py
# @Software: PyCharm
from pydantic import BaseModel, BaseConfig, BaseSettings
from functools import lru_cache

from Config import env


class RedConfig(BaseSettings):
    host: str
    port: int
    password: str
    minsize: int = 10
    maxsize: int = 10
    encoding:str="utf-8"
    decode_responses:bool = True

class DevRedConfig(RedConfig):
    host = ''
    port = 0
    password = ''


class ProRedConfig(RedConfig):
    host = ''
    port = 0
    password = ''


@lru_cache()
def register_config() -> RedConfig:
    return dict(
        dev=DevRedConfig,
        por=ProRedConfig,
    )[env]()


redconf = register_config()
