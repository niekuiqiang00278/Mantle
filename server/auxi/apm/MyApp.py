#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 19:32
# @Author  : cap669
# @File    : MyApp.py
# @Software: PyCharm
import time

from cacheout import Cache
import bcrypt, asyncio
from root.utils.StateUtils import StateUtils
from server.auxi.apm.base.wrapper.UecWrapper import UecWrapper
from server.auxi.model.LoAuModel import LoginModel
from fastapi import WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import Any


class CallModel(BaseModel):
    act: str
    por: str
    data: Any


class MyApp:
    def __init__(self):
        self.avem = 'avem'
        self.cache = Cache()
        self.user_list = {'cap669': {'pw': 'absdcc', 'aka': 'akacap669'}, 'cand': {'pw': 'absdcc', 'aka': 'akacand'},
                          'slou': {'pw': 'absdcc', 'aka': 'akaslou'}, 'dwac': {'pw': 'absdcc', 'aka': 'akadwac'},
                          'tran': {'pw': 'absdcc', 'aka': 'akatran'}, 'kuff': {'pw': 'absdcc', 'aka': 'akakuff'},
                          'reep': {'pw': 'absdcc', 'aka': 'akareep'}, 'cusm': {'pw': 'absdcc', 'aka': 'akacusm'},
                          'posh': {'pw': 'absdcc', 'aka': 'akaposh'}, 'she': {'pw': 'absdcc', 'aka': 'akashe'},
                          'psel': {'pw': 'absdcc', 'aka': 'akapsel'}, 'psek': {'pw': 'absdcc', 'aka': 'akapsek'},
                          'fut': {'pw': 'absdcc', 'aka': 'akafut'}, 'bift': {'pw': 'absdcc', 'aka': 'akabift'},
                          'rhot': {'pw': 'absdcc', 'aka': 'akarhot'}, 'jad': {'pw': 'absdcc', 'aka': 'akajad'},
                          'kim': {'pw': 'absdcc', 'aka': 'akakim'}}

    @UecWrapper()
    def adds(self, item: LoginModel, state: StateUtils):
        d0 = self.user_list.get(item.us)
        pw = d0.get('pw')
        k0 = {}
        try:
            if bcrypt.checkpw(pw.encode('utf-8'), str.encode(item.pw)):
                aka = d0.get('aka')
                k0.update(dict(aka=aka, por='por' + item.us, us=item.us, ws=False))
                self.cache.add(aka, k0, 15)
                state.succ(1, '登录成功')
            else:
                state.errn('登录失败')
        except:
            state.errn('登录失败')
        return k0, state

    @UecWrapper()
    def cheack(self, aka: str, por: str, state: StateUtils):
        d0 = self.cache.get(aka, None)
        if d0:
            d1 = d0.get('por', None)
            if d1:
                if bcrypt.checkpw(d1.encode('utf-8'), str.encode(por)):
                    state.succ(1, '校验成功')
                else:
                    state.errn('校验失败')
        return state

    @UecWrapper()
    def ck(self, aka: str, state: StateUtils,func0=None,func3=None):
        d0 = self.cache.get(aka, None)
        if d0:
            if func0:
                func0(d0)
            if func3:
                func3(d0)
            state.succ(1, 'aka')
        else:
            state.errn('ak')
        return state

    @UecWrapper()
    def keep(self, aka: str, state: StateUtils):
        if self.cache.get(aka):
            self.cache._expire_times[aka] = self.cache.timer() + 15
            state.succ(1, '延长成功')
        else:
            state.errn('延长失败')
        return state

    def dels(self, aka: str):
        state, us = self.down(aka)
        if state.code == 1:
            d0 = self.user_list.get(us, None)
            if d0:
                del self.user_list[us]
            else:
                state.errn('用户不存在')
        return state

    @UecWrapper()
    def down(self, aka: str, state: StateUtils) -> (StateUtils, str):
        d0 = self.cache.get(aka, None)
        us = None
        if d0:
            us = d0.get('us', None)
            if us:
                self.cache.delete(aka)
                state.succ(1, '删除成功')
            else:
                state.errn('us错误')
        else:
            state.errn('aka不存在')
        return state, us

    def depshow(self):
        t = time.time()
        b0 = []
        b1 = self.cache.expire_times()
        for us, v in self.user_list.items():
            aka = v.get('aka')
            d2 = self.cache.get(aka)
            live = -1
            if d2:
                live = int(b1.get(aka) - t)
            else:
                d2 = dict(ws=False,us=us,aka=aka,por='nuxx')
            f = dict(live=live)
            f.update(d2)
            b0.append(f)
        return b0
    async def websocket(self, ws: WebSocket, aka: str, call):
        def func0(d0):
            d0['ws'] = True
        state0:StateUtils = self.ck(aka,func0=func0)
        # js = 0
        if state0.code == 1:
            await ws.accept()
            # await ws.send_text(aka)
            while True:
                try:
                    t = await asyncio.wait_for( ws.receive_json(),1)
                    data = CallModel(**t)
                    if data.act == 'cheack':
                        state3:StateUtils = self.cheack(aka,data.por)
                        if state3.code == 1:
                            self.keep(aka)
                    else:
                        call(data)
                except asyncio.TimeoutError:
                    # js += 1
                    state1:StateUtils = self.ck(aka)
                    if state1.code == 1:
                        pass
                    else:
                        break
                except WebSocketDisconnect:
                    break
                except:
                    pass
            def func3(d0):
                d0['ws'] = False
            state3: StateUtils = self.ck(aka,func3=func3)


apm = MyApp()
# us = 'cap669'
# k0, state = apm.adds(LoginModel(**dict(us=us, pw='$2a$12$8RS227KstayHFO10FWO51eSo6YYCvxWB7gsa5/33aUlpbZhK.nvBO')))
# apm.adds(LoginModel(**dict(us='cand', pw='$2a$12$8RS227KstayHFO10FWO51eSo6YYCvxWB7gsa5/33aUlpbZhK.nvBO')))
if __name__ == '__main__':
    pass
    # salt = bcrypt.gensalt(prefix=b"2a")
    # password = "akacap669"
    # hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    # print(hashed_password)
    # apm.cheack('akacap669', '$2a$12$LtZMuXXIkSWCe.B12wpQI.diRQc5/VR/HGSR2byFWpKfAKTWMBjci')
    # apm.cache._expire_times['akacap669'] = apm.cache.timer() + 10
    # time.sleep(2)
    # t = time.time()
    # for k, v in apm.cache.expire_times().items():
    #     print(k, int(v - t))
