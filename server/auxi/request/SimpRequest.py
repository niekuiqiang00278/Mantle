#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/12 20:34
# @Author  : cap669
# @File    : SimpRequest.py
# @Software: PyCharm
from typing import Optional,Dict,Any
from fastapi import Request

from server.auxi.response.ApiResponse import ApiResponse


class Phuy:
    __state_code: int = 200
    __code: int = 0
    __msg: str =''
    __result:Optional[Dict[str, Any]]  = {}
    def show(self):
        return ApiResponse(self.__state_code, self.__code, self.__result, self.__msg)

    def get_msg(self) -> str:
        return self.__msg

    def set_msg(self, msg: str) -> None:
        self.__msg = msg

    def get_code(self) -> int:
        return self.__code

    def set_code(self, code: int) -> None:
        self.__code = code

    def get_state_code(self) -> int:
        return self.__state_code

    def set_state_code(self, state_code: int):
        self.__state_code = state_code

    def get_result(self):
        return self.__result

    def set_result(self, result):
        self.__result = result


class SimpRequest(Request):
    phuy: Phuy
