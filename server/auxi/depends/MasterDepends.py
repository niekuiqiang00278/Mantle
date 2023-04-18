#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/14 1:29
# @Author  : cap669
# @File    : MasterDepends.py
# @Software: PyCharm
# from abc import ABC,ABCMeta,abstractmethod
from server.auxi.depends.SimpDepends import SimpDepends
from server.auxi.request.SimpRequest import Phuy
from server.auxi.apm.MyApp import MyApp
class MasterDepends(SimpDepends):
    def __init__(self,apm):
        self.apm:MyApp = apm

    def set_phuy(self,phuy:Phuy):

        pass