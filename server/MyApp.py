from server.base.rpc.MRpc import MRpc
from server.fragment.ClientFragment import ClientFragment
from server.fragment.GodFragment import GodFragment
from server.fragment.MasterFragment import MasterFragment
from server.fragment.MsFragment import MsFragment
from server.plux.XActivity import XActivity
from fastapi import FastAPI
'C:\Kac\Tool\ffmpeg-master-latest-win64-gpl\bin'
import matplotlib
class MyApp(XActivity):
    def __init__(self):
        XActivity.__init__(self)

    def bis(self):
        pass

    def rpc(self):
        self.m = MRpc()
        # pass

    def fragment(self, app: FastAPI):
        MsFragment(app,self.m)
        GodFragment(app)
        # MasterFragment(app)
        # ClientFragment(app)


if __name__ == '__main__':
    MyApp()
