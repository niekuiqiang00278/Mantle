#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 1:35
# @Author  : cap669
# @File    : MRpc.py
# @Software: PyCharm
from root.config.RpcConfig import rpcconf
from root.plux.XRpc import RpcCl, ClInjection
from root.rpc import hello_pb2_grpc, hello_pb2
@ClInjection(host=rpcconf.host, port=rpcconf.port)
class MRpc(RpcCl):
    def __init__(self):
        RpcCl.__init__(self)

    def m0(self):
        message = None
        with self.register_channel() as channel:
            stub = hello_pb2_grpc.GreeterStub(channel)
            response = stub.SayHello(hello_pb2.HelloRequest(name='小钟同学'))
            message = response.message
        return message
# Tips     :
