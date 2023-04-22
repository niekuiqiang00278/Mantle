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
    stub0 = None

    def __init__(self):
        RpcCl.__init__(self)

    def register_stub(self, channel):
        self.stub0 = hello_pb2_grpc.GreeterStub(channel)

    def m0(self):
        response = self.stub0.SayHello(hello_pb2.HelloRequest(name='小钟同学'))
        message = response.message
        print(message)


if __name__ == '__main__':
    m = MRpc()
    m.m0()

# Tips     :
