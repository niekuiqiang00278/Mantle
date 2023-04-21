#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 23:57
# @Author  : cap669
# @File    : XJob.py
# @Software: PyCharm
import traceback

from peewee import Model
from playhouse.pool import PooledPostgresqlDatabase
from root.base.wrapper.EvsWrapper import EvsWrapper
from root.utils.StateUtils import StateUtils
from root.utils.Utils import Utils
from typing import Any, List


class XHis0:
    def __init__(self, cur: Model, safe_table: bool, clear_table: bool, func):
        if safe_table:
            if cur.table_exists():
                if clear_table:
                    cur.truncate_table()
            else:
                cur.create_table()
        if func:
            func()
        self.cur = cur


class XJob0(XHis0):
    def __init__(self, cur: Model, db: PooledPostgresqlDatabase, safe_table: bool = True, clear_table: bool = False,
                 func: Any = None):
        XHis0.__init__(self, cur, safe_table, clear_table, func)
        self.db = db

    @EvsWrapper()
    def adds(self, info: str, state: StateUtils):
        d0 = dict(
            uid=Utils.f1(),
            info=info,
            ctime=Utils.u0()
        )
        with self.db.atomic():
            e0 = self.cur.insert_many(d0).execute()
            if e0:
                state.succ(1)
            else:
                state.errn()
        return state

    @EvsWrapper()
    def addc(self, data: List[str], state: StateUtils):
        ctime = Utils.u0()
        with self.db.atomic():
            try:
                d0 = [dict(uid=Utils.f1(), ctime=ctime, info=info) for info in data]
                self.cur.insert_many(d0) \
                    .on_conflict_ignore() \
                    .execute()
                state.succ(1, '')
            except:
                state.errn('')
        return state

    @EvsWrapper()
    def comp(self, func, uid: str, state: StateUtils, msg: str = 'nuxx'):
        d0 = self.cur.select().where(self.cur.uid == uid).for_update().get()
        d0.msg = msg
        d0.stime = Utils.u0()
        with self.db.manual_commit():
            try:
                state1: StateUtils = func()
                if state1.code == 1:
                    d0.fnsh = 4
                else:
                    d0.fnsh = 3
                d0.save()
                state.succ(1, state1.get_msg())
            except:
                print(traceback.format_exc())
                state.errn('')
        return state

    @EvsWrapper()
    def gets(self, aka: str, state: StateUtils, msg: str = 'nuxx'):
        uid, info = '', ''
        with self.db.atomic():
            d0 = self.cur.select().where(self.cur.fnsh == 1).for_update().get()
            d0.rtime = Utils.u0()
            d0.fnsh = 2
            d0.msg = msg
            d0.aka = aka
            if d0.save():
                state.succ(1)
                uid = d0.uid
                info = d0.info
            else:
                state.errn()
        return state, uid, info

    @EvsWrapper()
    def outs(self, aka: str, state: StateUtils, msg: str = 'nuxx'):
        with self.db.atomic():
            d0 = self.cur.select().where(self.cur.aka == aka).for_update().get()
            d0.rtime = Utils.u0()
            d0.fnsh = 1
            d0.msg = msg
            d0.save()
            if d0.save():
                state.succ(1)
            else:
                state.errn()
        return state

    def show(self):
        d0 = self.cur.select()
        bag = []
        if d0:
            for d1 in d0:
                d3 = d1.__data__
                bag.append(d3)
        return bag


class XJob1(XHis0):
    def __init__(self, cur: Model, db: PooledPostgresqlDatabase, safe_table: bool = True, clear_table: bool = False,
                 func: Any = None):
        XHis0.__init__(self, cur, safe_table, clear_table, func)
        self.db = db

    def adds(self):
        pass

    def comp(self):
        pass

    @EvsWrapper()
    def gets(self,state:StateUtils, uid=None):
        if uid:
            state.succ(1,'更具uid寻找任务')

        if state.code == 1:
            pass
        else:
            state.succ(1,'新任务')
    def outs(self):
        pass

    def show(self):
        pass


class XJob2:
    def __init__(self):
        pass

# Tips     :支持任务分布式分发,允许中断,
