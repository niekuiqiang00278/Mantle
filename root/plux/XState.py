from typing import List, Any


class XState:
    def __init__(self):
        self.code: int = 0
        self.msg: List[Any] = []

    def add_msg(self, type: str, msg: str):
        self.msg.append(
            dict(
                code=self.code,
                dt='',
                type=type,
                msg=msg,
            )
        )

    def succ(self, code: int, msg: str = 'nuxx'):
        self.code = code
        self.add_msg('succ', msg)

    def wran(self, msg: str = 'nuxx'):
        self.code = -1
        self.add_msg('wran', msg)

    def errn(self, msg: str = 'nuxx'):
        self.code = -1
        self.add_msg('errn', msg)

    def __call__(self, func):
        pass


class XSkin:
    def __init__(self):
        pass

    def __call__(self, func):
        pass
