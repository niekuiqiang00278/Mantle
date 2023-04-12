#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/12 20:32
# @Author  : cap669
# @File    : SimpDepends.py
# @Software: PyCharm
from server.auxi.request.SimpRequest import SimpRequest
class SimpDepends:
    def __call__(self,request:SimpRequest) -> SimpRequest:
        return request
