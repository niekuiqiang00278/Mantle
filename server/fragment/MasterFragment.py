#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/12 20:44
# @Author  : cap669
# @File    : MasterFragment.py
# @Software: PyCharm
# from abc import ABC,ABCMeta,abstractmethod
from fastapi import APIRouter, Depends
from server.auxi.depends.SimpDepends import SimpDepends
from server.plux.XFragment import XFragment, FragmentInjection


@FragmentInjection(prefix='/master', dependencies=[Depends(SimpDepends())])
class MasterFragment(XFragment):
    def __init__(self, app):
        XFragment.__init__(self, app)

    def register_router(self, router: APIRouter):
        pass
