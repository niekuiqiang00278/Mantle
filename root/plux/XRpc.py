#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 1:24
# @Author  : cap669
# @File    : XRpc.py
# @Software: PyCharm
# from abc import ABC,ABCMeta,abstractmethod
from concurrent import futures

import grpc


def SeRpcInjection(port: str):
    def back(cls):
        cls.port = port
        return cls

    return back


class XRpcSe:
    port: str

    def __init__(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self.register_rpc(server)
        server.add_insecure_port(f'[::]:{self.port}')
        server.start()
        server.wait_for_termination()

    def register_rpc(self, server):
        pass


# Tips     :

def ClInjection(host: str, port: int):
    def back(cls):
        cls.host = host
        cls.port = port
        return cls

    return back


class RpcCl:
    host: str
    port: int

    def __init__(self):
        self.register_stub(grpc.insecure_channel(f'{self.host}:{self.port}'))

    def register_stub(self, channel):
        pass
