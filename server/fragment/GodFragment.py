#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/17 23:08
# @Author  : cap669
# @File    : GodFragment.py
# @Software: PyCharm
from fastapi import FastAPI, Depends, APIRouter

from root.utils.StateUtils import StateUtils
from server.auxi.apm.MyApp import apm
from server.auxi.depends.SimpDepends import SimpDepends
from server.auxi.model.LoAuModel import LoginModel, AuthModel
from server.auxi.request.SimpRequest import SimpRequest
from server.plux.XFragment import FragmentInjection, XFragment
@FragmentInjection(prefix='/god', dependencies=[Depends(SimpDepends())])
class GodFragment(XFragment):
    def __init__(self, app: FastAPI):
        XFragment.__init__(self, app)

    def register_router(self, router: APIRouter):
        @router.post('/userlist')
        async def userlist(request:SimpRequest):
            request.phuy.set_result(apm.user_list)
            return request.phuy.show()

        @router.post('/login')
        async def login(request:SimpRequest,item: LoginModel):
            k0,state = apm.adds(item)
            request.phuy.set_result(k0)
            request.phuy.set_code(state.get_code())
            request.phuy.set_msg(state.get_msg())
            return request.phuy.show()


        @router.get('/readme')
        async def readme(request:SimpRequest):
            request.phuy.set_result([
                dict(url='/test', method='post',tag=''),
            ])
            return request.phuy.show()


        @router.post('/depshow')
        async def depshow(request:SimpRequest):
            request.phuy.set_result(apm.depshow())
            return request.phuy.show()


        @router.post('/keep')
        async def keep(request:SimpRequest,item: AuthModel):
            d0: StateUtils = apm.cheack(item.aka,item.por)
            if d0.code == 1:
                apm.keep(item.aka)
            request.phuy.set_result(d0.get_code())
            request.phuy.set_msg(d0.get_msg())
            return request.phuy.show()