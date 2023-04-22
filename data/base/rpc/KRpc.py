#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 1:25
# @Author  : cap669
# @File    : KRpc.py
# @Software: PyCharm
from root.plux.XRpc import XRpcSe, SeRpcInjection
from root.config.RpcConfig import rpcconf
from root.rpc import hello_pb2_grpc, hello_pb2


class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message='hello {msg}'.format(msg=request.name))

    def SayHelloAgain(self, request, context):
        return hello_pb2.HelloReply(message='hello {msg}'.format(msg=request.name))


@SeRpcInjection(port=rpcconf.port)
class KRpc(XRpcSe):
    def register_rpc(self, server):
        hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
if __name__ == '__main__':
    KRpc()

# Tips     :
