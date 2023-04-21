#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/22 2:27
# @Author  : cap669
# @File    : SamBis.py
# @Software: PyCharm
from data.base.Cur import janbase
from data.base.cur.JanCur import Jan1Cur
from root.plux.XJob import XJob1


class SamBis(XJob1):
    def __init__(self):
        XJob1.__init__(self,Jan1Cur,janbase,clear_table=True)


if __name__ == '__main__':
    sam = SamBis()


# Tips     :
