from data.base.Dmd import Dmd
from data.base.rpc.KRpc import KRpc
from data.bis.KemBis import KemBis
from data.plux.XActivity import XActivity


class MyApp(XActivity):
    def __init__(self):
        XActivity.__init__(self)

    def base(self):
        # Dmd()
        pass

    def bis(self):
        self.kem = KemBis()

    def rpc(self):
        self.k = KRpc()
        pass

if __name__ == '__main__':
    data = MyApp()
