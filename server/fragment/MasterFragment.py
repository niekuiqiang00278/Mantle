#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/12 20:44
# @Author  : cap669
# @File    : MasterFragment.py
# @Software: PyCharm
# from abc import ABC,ABCMeta,abstractmethod
from fastapi import APIRouter, Depends

from server.auxi.apm.MyApp import apm
from server.auxi.depends.MasterDepends import MasterDepends
from server.plux.XFragment import XFragment, FragmentInjection


@FragmentInjection(prefix='/master', dependencies=[Depends(MasterDepends(apm=apm))])
class MasterFragment(XFragment):
    def __init__(self, app):
        XFragment.__init__(self, app)

    def register_router(self, router: APIRouter):
        @router.post('/dels')
        async def dels():
            pass

        @router.post('/down')
        async def down():
            pass

        @router.post('/watch')
        async def watch():
            pass
