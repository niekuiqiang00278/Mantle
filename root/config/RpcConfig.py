#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 1:32
# @Author  : cap669
# @File    : RpcConfig.py
# @Software: PyCharm
# from abc import ABC,ABCMeta,abstractmethod

from pydantic import BaseModel, BaseConfig, BaseSettings
from functools import lru_cache

from Config import env


class RpcConfig(BaseSettings):
    host:str = 'localhost'
    port: int
    max_workers: int=10

class DevRpcConfig(RpcConfig):
    port = 50051


class ProRpcConfig(RpcConfig):
    port = 0


@lru_cache()
def register_config() -> RpcConfig:
    return dict(
        dev=DevRpcConfig,
        por=ProRpcConfig,
    )[env]()


rpcconf = register_config()

# Tips     :
