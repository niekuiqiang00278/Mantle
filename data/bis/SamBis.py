#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/22 2:27
# @Author  : cap669
# @File    : SamBis.py
# @Software: PyCharm
from data.base.Cur import janbase
from data.base.cur.JanCur import Jan1Cur
from root.plux.XJob import XJob1

from json import dumps, loads


class SamBis(XJob1):
    def __init__(self):
        XJob1.__init__(self, Jan1Cur, janbase, clear_table=True)

    def __ec0(self, name: str, w: str):
        return dict(
            name=name, w=w
        )

    def sam0(self, name, w):
        d0 = self.__ec0(name, w)
        d1 = dumps(d0)
        self.adds(
            info=d1, an=10, en=0
        )

    def sam1(self, aka):
        state, uid, info = self.gets(aka)
        return uid,info

    def sam2(self,uid):
        self.comp(uid)

if __name__ == '__main__':
    e1 = 'blem'
    e2 = 'wash'
    e0 = ['od', e1, 'fuc', 'vupt', e2, 'vuff', 'yaw', 'tusk', 'coss', 'saic', 'bapt', 'kuy', 'mald', 'shaw', 'legh']
    sam = SamBis()
    akacand = 'akacand'
    akacap669 = 'akacap669'
    sam.sam0(e1, e2)
    sam.sam0('aa','bb')
    uid,info = sam.sam1(akacand)
    sam.sam2(uid)
# Tips     :
