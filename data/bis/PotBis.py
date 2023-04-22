#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/22 2:34
# @Author  : cap669
# @File    : PotBis.py
# @Software: PyCharm
# from abc import ABC,ABCMeta,abstractmethod
from data.base.Cur import janbase
from data.base.cur.JanCur import Jan2Cur
from root.base.wrapper.EvsWrapper import EvsWrapper
from root.plux.XJob import XJob2
from json import loads, dumps

from root.utils.StateUtils import StateUtils


class PotBis(XJob2):
    def __init__(self):
        XJob2.__init__(self, Jan2Cur, janbase, clear_table=True)

    def pot0(self, name: str):
        self.adds(name)

    def pot1(self):
        pass

    def pot2(self, uid,diff):
        @EvsWrapper()
        def func(state:StateUtils):
            state.succ(1)
            return state

        self.comp(func, uid,diff)

    def pot3(self, aka: str,info, diff):
        state, uid = self.gets(aka,info, diff)
        return uid

    def pot4(self):
        pass


if __name__ == '__main__':
    e1 = 'blem'
    e2 = 'wash'
    e0 = ['od', e1, 'fuc', 'vupt', e2, 'vuff', 'yaw', 'tusk', 'coss', 'saic', 'bapt', 'kuy', 'mald', 'shaw', 'legh']
    pot = PotBis()
    akacand = 'akacand'
    akacap669 = 'akacap669'
    for e in e0:
        pot.pot0(e)
    uid  = pot.pot3(akacand,e1, 2)
    pot.pot2(uid,2)



# Tips     :
