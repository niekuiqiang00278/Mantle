#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/22 2:27
# @Author  : cap669
# @File    : SamBis.py
# @Software: PyCharm
from json import load

from pydantic import BaseModel

from typing import Any
class Main:
    def __init__(self):
        from json import dump
        with open("data.json", encoding='UTF-8', mode="r") as f:
            user_dict = {
                "id": {
                    'ws':[1,2,3,4]
                },
                "name": "John Doe",
                "email": "johndoe@example.com",
                "ww": {
                    'wwc': {
                        'ff':2
                    }
                }
            }
            User = type("User", (BaseModel,), user_dict)
            class Fm(BaseModel):
                title:str
                type:str
                properties:dict

            class Qm(BaseModel):
                title:str
                default:Any
                type:str
            m = []
            def f0(d0:Fm,js = -1):
                js += 1
                q2 = 'Class {}Model{}(BaseModel):\n{}'
                q3 = []
                for k,v in d0.properties.items():
                    z = Qm(**v)
                    e = type(z.default)
                    if e == dict:
                        b = type(z.title, (BaseModel,), z.default)
                        q0 = f'    {z.title}:{z.title}Model'
                        q3.append(q0)
                        f0(Fm(**b.schema()),js)
                    elif e == list:
                        for n in z.default:
                            h = type(n)
                            f = 'Any'
                            if h == str:
                                f = 'str'
                            elif h == int:
                                f = 'int'
                            elif h == float:
                                f = 'float'
                            j = f'List[{f}]'
                            print(j)

                        # b = type(z.title, (BaseModel,), dict(ff=3))
                        # print(z.title,z.default,z.type)
                    else:
                        f = 'Any'
                        if e == str:
                            f = 'str'
                        elif e == int:
                            f = 'int'
                        elif e == float:
                            f = 'float'
                        q0 = f'    {z.title}:{f}'
                        q3.append(q0)

                m.append(q2.format(d0.title,js,'\n'.join(q3)))
            f0(Fm(**User.schema()))
            # print(User.schema())
            f.close()
            print('\n'.join(m))


def server(self):
    pass


if __name__ == '__main__':
    Main()
