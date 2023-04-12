from server.fragment.ClientFragment import ClientFragment
from server.fragment.MasterFragment import MasterFragment
from server.fragment.MsFragment import MsFragment
from server.plux.XActivity import XActivity
from fastapi import FastAPI


class MyApp(XActivity):
    def __init__(self):
        XActivity.__init__(self)

    def fragment(self, app: FastAPI):
        MsFragment(app)
        MasterFragment(app)
        ClientFragment(app)


if __name__ == '__main__':
    MyApp()
