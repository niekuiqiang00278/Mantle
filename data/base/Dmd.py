#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 2:41
# @Author  : cap669
# @File    : Dmd.py
# @Software: PyCharm
from cmd import Cmd
from threading import Thread
import argparse

class Dmd(Cmd):
    prompt = 'dmd> '

    def __init__(self):
        Cmd.__init__(self)
        Thread(target=self.cmdloop).start()

    def do_greet(self, line):
        parser = argparse.ArgumentParser(description='Description of your program')
        parser.add_argument('-n', '--name', type=str, help='Description of name argument')
        parser.add_argument('-hi', '--hide', type=str, help='Description of name argument')
        args, unknown = parser.parse_known_args(line.split())
        print(args.hide)
    def do_quit(self, line):
        pass

    def emptyline(self) -> bool:
        pass


if __name__ == '__main__':
    Dmd()

# Tips     :
