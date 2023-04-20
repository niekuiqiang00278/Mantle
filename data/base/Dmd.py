#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 2:41
# @Author  : cap669
# @File    : Dmd.py
# @Software: PyCharm
# from abc import ABC,ABCMeta,abstractmethod
from cmd import Cmd
from threading import Thread


class Dmd(Cmd):
    prompt = 'dmd> '

    def __init__(self):
        Cmd.__init__(self)
        Thread(target=self.cmdloop).start()

    def do_greet(self, line):
        pass

    def do_quit(self, line):
        pass

    def emptyline(self) -> bool:
        pass


if __name__ == '__main__':
    Dmd()

# Tips     :
