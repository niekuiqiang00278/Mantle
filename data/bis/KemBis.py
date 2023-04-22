#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 23:50
# @Author  : cap669
# @File    : KemBis.py
# @Software: PyCharm
from data.base.Cur import janbase
from data.base.cur.JanCur import Jan0Cur
from root.base.wrapper.EvsWrapper import EvsWrapper
from root.plux.XJob import XJob0
from pydantic import BaseModel
from json import loads, dumps
from typing import List

from root.utils.StateUtils import StateUtils


class EcModel(BaseModel):
    name: str
    w: str


class KemBis(XJob0):
    def __init__(self):
        XJob0.__init__(self, Jan0Cur, janbase, clear_table=True)

    def __ec1(self, data: str):
        return EcModel(**loads(data))

    def __ec0(self, name: str, w: str):
        return dict(
            name=name, w=w
        )

    @EvsWrapper()
    def ke0(self, name: str, w: str, state: StateUtils):
        try:
            d0 = EcModel(name=name, w=w)
            d1 = dumps(d0.dict())
            self.adds(info=d1, state=state)
        except:
            state.errn('')
        return state

    @EvsWrapper()
    def ke11(self, data: List[EcModel], state: StateUtils):
        def func(d0: EcModel):
            return dumps(d0.dict())

        self.addc(data=data, func=func, state=state)
        return state

    @EvsWrapper()
    def ke1(self, uid, state: StateUtils):
        @EvsWrapper()
        def func(state: StateUtils):
            state.errn()
            return state

        return self.comp(func=func, uid=uid, state=state)

    @EvsWrapper()
    def ke2(self, aka: str, state: StateUtils):
        uid, info = self.gets(aka=aka, state=state)
        name, w = '', ''
        if state.code == 1:
            d0 = self.__ec1(info)
            name = d0.name
            w = d0.w
        return uid, name, w, state

    @EvsWrapper()

    def ke3(self, aka: str, state: StateUtils):
        self.outs(aka=aka,state=state)

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
        kem.ke0(e1, 2)
        uid, name, w, state = kem.ke2(akacand)
        kem.ke3(akacand)
        # if state.code == 1:
        #     state = kem.ke1(uid)


    def func1():
        f = []
        for e in e0:
            z = EcModel(name=e, w=e)
            f.append(z)
        kem.ke11(f)
        uid, name, w, state = kem.ke2(akacand)
        if state.code == 1:
            state = kem.ke1(uid)


    f = 0
    if f == 0:
        func0()
    elif f == 1:
        func1()
# Tips     :
