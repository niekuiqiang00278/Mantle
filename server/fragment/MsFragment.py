from server.auxi.apm.MyApp import apm,CallModel
from server.auxi.depends.SimpDepends import SimpDepends
from server.auxi.model.LoAuModel import LoginModel
from server.plux.XFragment import XFragment, FragmentInjection
from fastapi import FastAPI, APIRouter, Depends,WebSocket,WebSocketDisconnect


@FragmentInjection(prefix='/ffw', dependencies=[Depends(SimpDepends())])
class MsFragment(XFragment):
    def __init__(self, app: FastAPI):
        XFragment.__init__(self, app)

    def register_router(self, router: APIRouter):
        @router.post('/fff')
        async def fff():
            pass

        @router.post('/login')
        async def login(item: LoginModel):
            return apm.adds(item)

        @router.websocket('/test/{aka}')
        async def test(ws:WebSocket,aka:str):
            def call(data:CallModel):
                print(aka,data)
            await apm.websocket(ws,aka,call)



