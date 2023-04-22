#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/22 2:27
# @Author  : cap669
# @File    : SamBis.py
# @Software: PyCharm
from data.base.Cur import janbase
from data.base.cur.JanCur import Jan1Cur
from root.base.wrapper.EvsWrapper import EvsWrapper
from root.plux.XJob import XJob1
from typing import Any, Dict
from json import dumps, loads
from pydantic import BaseModel
from root.utils.StateUtils import StateUtils




class EwModel(BaseModel):
    name: str
    w: str


class SamBis(XJob1):
    def __init__(self):
        XJob1.__init__(self, Jan1Cur, janbase, clear_table=True)

    def __ec1(self, data: str):
        return EwModel(**loads(data))

    def __ec0(self, name: str, w: str):
        d0 = EwModel(name=name, w=w)
        return d0.dict()

    @EvsWrapper()
    def sam0(self, name, w, state: StateUtils):
        d0 = self.__ec0(name, w)
        d1 = dumps(d0)
        self.adds(info=d1, state=state, an=2, en=0)

    @EvsWrapper()
    def sam1(self, aka, state: StateUtils):
        uid, info = self.gets(aka=aka, state=state)
        return uid, info
    @EvsWrapper()
    def sam2(self, uid, state: StateUtils):
        @EvsWrapper()
        def func(state:StateUtils):
            state.succ(1)
            return state
        self.comp(uid=uid,func=func,state=state)

    @EvsWrapper()
    def sam3(self,aka,state:StateUtils):
        self.outs(aka=aka,state=state)

if __name__ == '__main__':
    e1 = 'blem'
    e2 = 'wash'
    e0 = ['od', e1, 'fuc', 'vupt', e2, 'vuff', 'yaw', 'tusk', 'coss', 'saic', 'bapt', 'kuy', 'mald', 'shaw', 'legh']
    sam = SamBis()
    akacand = 'akacand'
    akacap669 = 'akacap669'
    sam.sam0(e1, e2)
    # sam.sam0('aa', 'bb')
    uid, info = sam.sam1(akacand)
    sam.sam2(uid)
    sam.sam2(uid)
    sam.sam2(uid)
    sam.sam2(uid)
    sam.sam3(akacand)
# Tips     :
