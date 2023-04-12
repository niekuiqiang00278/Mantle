#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/12 20:42
# @Author  : cap669
# @File    : LoAuModel.py
# @Software: PyCharm
from pydantic import BaseModel


class LoginModel(BaseModel):
    us: str
    pw: str


class AuthModel(BaseModel):
    aka: str
    por: str
