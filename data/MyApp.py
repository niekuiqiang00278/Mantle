from data.base.Dmd import Dmd
from data.base.rpc.KRpc import KRpc
from data.plux.XActivity import XActivity


class MyApp(XActivity):
    def __init__(self):
        XActivity.__init__(self)

    def base(self):
        # Dmd()
        pass

    def bis(self):
        pass

    def rpc(self):
        # self.k = KRpc()
        pass

if __name__ == '__main__':
    data = MyApp()
