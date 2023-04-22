#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/22 2:33
# @Author  : cap669
# @File    : XTask.py
# @Software: PyCharm
from threading import Thread
from apscheduler.schedulers.background import BackgroundScheduler

from root.utils.Utils import Utils
from typing import Dict, Any
from pydantic import BaseModel


class TaskModel:
    live: bool = True


class XTask:
    def __init__(self):
        self.sc = BackgroundScheduler()
        self.c: Dict[str, dict] = {}

    def adds(self, func):

        def run(uid):
            while True:
                d0 = self.c.get(uid)
                if d0['live']:
                    func()
        uid = Utils.f1()
        self.c[uid] = dict(live=True)
        self.sc.add_job(func=run,args=(uid,))


class XTas0:
    def __init__(self):
        self.live = True

    def run(self, func):
        while self.live:
            func()


class XTas1:
    def __init__(self):
        pass
# Tips     :
