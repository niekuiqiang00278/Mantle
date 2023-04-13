#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/12 20:44
# @Author  : cap669
# @File    : ClientFragment.py
# @Software: PyCharm
from fastapi import Depends, APIRouter
from server.auxi.depends.SimpDepends import SimpDepends
from server.auxi.model.LoAuModel import LoginModel
from server.plux.XFragment import XFragment, FragmentInjection


@FragmentInjection(prefix='/client', dependencies=[Depends(SimpDepends())])
class ClientFragment(XFragment):
    def __init__(self, app):
        XFragment.__init__(self, app)

    def register_router(self, router: APIRouter):
        @router.post('/login')
        async def login(item:LoginModel):
            pass
