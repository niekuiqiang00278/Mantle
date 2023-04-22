#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 23:57
# @Author  : cap669
# @File    : XJob.py
# @Software: PyCharm
import datetime
import traceback
from peewee import Model
from peewee import fn
from playhouse.pool import PooledPostgresqlDatabase
from root.base.wrapper.EvsWrapper import EvsWrapper
from root.utils.StateUtils import StateUtils
from root.utils.Utils import Utils
from typing import Any, List
from pydantic import BaseModel


class Job0Model(BaseModel):
    uid: str
    info: str
    ctime: datetime.datetime


class Job1Model(Job0Model):
    an: int
    en: int


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

    def adds(self, info: str, state: StateUtils):
        d0 = Job0Model(uid=Utils.f1(), info=info, ctime=Utils.u0())
        d1 = d0.dict()
        with self.db.atomic():
            e0 = self.cur.insert_many(d1).execute()
            if e0:
                state.succ(1)
            else:
                state.errn()
        return state

    def addc(self, data: List[Any], func: Any, state: StateUtils):
        ctime = Utils.u0()
        with self.db.atomic():
            try:
                d0 = [Job0Model(uid=Utils.f1(), ctime=ctime, info=func(d0)).dict() for d0 in data]
                self.cur.insert_many(d0) \
                    .on_conflict_ignore() \
                    .execute()
                state.succ(1, '')
            except:
                state.errn('')
        return state

    def comp(self, func, uid: str, state: StateUtils, msg: str = 'nuxx'):
        try:
            with self.db.manual_commit():
                d0 = self.cur.select().where(self.cur.uid == uid).for_update().get()
                sta: StateUtils = func()
                if sta.code == 1:
                    d0.fnsh = 4
                else:
                    d0.fnsh = 3
                d0.msg = msg
                d0.stime = Utils.u0()
                if d0.save():
                    state.succ(1, )
        except self.cur.DoesNotExist:
            state.errn('')
        return state

    def gets(self, aka: str, state: StateUtils, msg: str = 'nuxx'):
        uid, info = '', ''
        with self.db.atomic():
            try:
                d0 = self.cur.select().where(self.cur.fnsh == 1).limit(1).for_update().get()
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
            except self.cur.DoesNotExist:
                state.errn()

        return uid, info

    def outs(self, aka: str, state: StateUtils, msg: str = 'nuxx'):
        with self.db.atomic():
            try:
                d0 = self.cur.select().where((self.cur.fnsh == 2) & (self.cur.aka == aka)).for_update().get()
                d0.rtime = Utils.u0()
                d0.fnsh = 1
                if msg == 'nuxx':
                    msg = f'cur:{aka}'
                d0.msg = msg
                d0.aka = 'nuxx'
                if d0.save():
                    state.succ(1)
                else:
                    state.errn('')
            except self.cur.DoesNotExist:
                state.errn()

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

    def adds(self, info: str, state: StateUtils, an: int = 0, en: int = 0):
        if an >= en:
            d0 = Job1Model(uid=Utils.f1(), info=info, an=an, en=en, ctime=Utils.u0())
            d1 = d0.dict()
            with self.db.atomic():
                e0 = self.cur.insert_many(d1).execute()
                if e0:
                    state.succ(1)
                else:
                    state.errn()
        else:
            state.errn()
        return state

    def comp(self, uid,func, state: StateUtils):
        with self.db.atomic():
            try:
                d0 = self.cur.select().where((self.cur.fnsh == 2) & (self.cur.uid == uid)).for_update().get()
                if d0.an > d0.en:
                    sta:StateUtils = func()
                    if sta.code == 1:
                        d0.rtime = Utils.u0()
                        d0.en = d0.en + 1
                        if d0.save():
                            state.succ(1)
                            if d0.an == d0.en:
                                d0.fnsh = 4
                                if d0.save():
                                    state.succ(2)
                                else:
                                    state.errn('')
                        else:
                            state.errn()
                    else:
                        state.errn('')
                else:
                    state.errn('')
            except:
                state.errn()

    def outs(self,aka:str,state:StateUtils,msg:str = 'nuxx'):
        with self.db.atomic():
            try:
                d0 = self.cur.select().where((self.cur.fnsh == 2) & (self.cur.aka == aka)).for_update().get()
                d0.rtime = Utils.u0()
                d0.fnsh = 1
                if msg == 'nuxx':
                    msg = f'cur:{aka}'
                d0.msg = msg
                d0.aka = 'nuxx'
                if d0.save():
                    state.succ(1)
                else:
                    state.errn('')
            except self.cur.DoesNotExist:
                state.errn()


    def gets(self, aka: str, state: StateUtils, msg: str = 'nuxx'):
        uid, info = '', ''
        with self.db.atomic():
            if aka:
                try:
                    d0 = self.cur.select().where((self.cur.fnsh == 2) & (self.cur.aka == aka)).for_update().get()
                    d0.rtime = Utils.u0()
                    d0.fnsh = 2
                    d0.msg = msg
                    d0.aka = aka
                    d0.save()
                    state.succ(1, '更具aka寻找任务')
                    uid = d0.uid
                    info = d0.info
                except self.cur.DoesNotExist:
                    state.errn()
            if state.code == 1:
                pass
            else:
                try:
                    d0 = self.cur.select().where(self.cur.fnsh == 1).for_update().get()
                    d0.rtime = Utils.u0()
                    d0.fnsh = 2
                    d0.msg = msg
                    d0.aka = aka
                    if d0.save():
                        state.succ(1, '新任务')
                        uid = d0.uid
                        info = d0.info
                    else:
                        state.errn()
                except:
                    state.errn()
        return uid, info


    def show(self):
        pass


class XJob2(XHis0):
    def __init__(self, cur: Model, db: PooledPostgresqlDatabase, safe_table: bool = True, clear_table: bool = False,
                 func: Any = None):
        XHis0.__init__(self, cur, safe_table, clear_table, func)
        self.db = db

    @EvsWrapper()
    def adds(self, info, state: StateUtils):
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

    def addc(self):
        pass

    @EvsWrapper()
    def comp(self, func: Any, uid: str, diff: int, state: StateUtils, msg: str = 'nuxx'):
        with self.db.atomic():
            d0 = self.cur.select().where(self.cur.uid == uid).for_update().get()
            state0: StateUtils = func()
            if state0.code == 1:
                d0.diff = diff
                d0.stime = Utils.u0()
                d0.msg = msg
                d0.aka = 'nuxx'
                d0.save()
                state.succ(1)
            else:
                state.errn()

    def outs(self, aka: str):
        pass

    @EvsWrapper()
    def gets(self, aka: str, info: str, diff: int, state: StateUtils, msg: str = 'nuxx'):
        uid = ''
        with self.db.atomic():
            try:
                d0 = self.cur.select().where((self.cur.diff != diff) & (self.cur.info == info)).order_by(
                    fn.Random()).limit(1).for_update().get()
                d0.rtime = Utils.u0()
                d0.msg = msg
                d0.aka = aka
                d0.save()
                state.succ(1)
                uid = d0.uid
            except self.cur.DoesNotExist:
                state.errn()
        return state, uid

    def show(self):
        pass

# Tips     :XJob0,XJob1 可以执行分布式运算 XJob2 只能同步运算
