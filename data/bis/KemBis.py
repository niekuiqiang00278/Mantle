#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 23:50
# @Author  : cap669
# @File    : KemBis.py
# @Software: PyCharm
from data.base.Cur import janbase
from data.base.cur.JanCur import Jan0Cur
from root.base.wrapper.EvsWrapper import EvsWrapper
from root.plux.XBis import XBis0
from pydantic import BaseModel
from json import loads, dumps
from typing import List

from root.utils.StateUtils import StateUtils


class EcModel(BaseModel):
    name: str
    w: str


class KemBis(XBis0):
    def __init__(self):
        XBis0.__init__(self, Jan0Cur, janbase, clear_table=True)

    def __ec1(self, data: str):
        return EcModel(**loads(data))

    def __ec0(self, name: str, w: str):
        return dict(
            name=name, w=w
        )

    @EvsWrapper()
    def ke0(self, name: str, w: str, state: StateUtils):
        d0 = self.__ec0(name, w)
        d1 = dumps(d0)
        self.adds(
            info=d1
        )

    def ke11(self, data: List[str]):
        self.addc(
            data
        )

    def ke1(self,uid):
        @EvsWrapper()
        def func(state: StateUtils):
            state.succ(1)
            return state
        return self.comp(
            func,uid
        )

    def ke2(self, aka: str):
        state,uid, info = self.gets(
            aka
        )
        name, w = '', ''
        if state.code == 1:
            d0 = self.__ec1(info)
            name = d0.name
            w = d0.w
        return uid,name, w

    def ke3(self, aka: str):
        state = self.outs(
            aka
        )

    def ke8(self):
        self.show()


if __name__ == '__main__':
    e1 = 'blem'
    e2 = 'wash'
    e0 = ['od', e1, 'fuc', 'vupt', e2, 'vuff', 'yaw', 'tusk', 'coss', 'saic', 'bapt', 'kuy', 'mald', 'shaw', 'legh']
    kem = KemBis()
    akacand = 'akacand'
    akacap669 = 'akacap669'


    def func0():
        kem.ke0(e1, e2)
        uid,name, w = kem.ke2(akacand)
        print(uid,name, w)
        state = kem.ke1(uid)
        print(state)


    def func1():
        kem.ke11(e0)
        kem.ke2(akacand)


    f = 0
    if f == 0:
        func0()
    elif f == 1:
        func1()
# Tips     :
