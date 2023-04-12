from server.auxi.depends.SimpDepends import SimpDepends
from server.auxi.model.LoAuModel import LoginModel
from server.plux.XFragment import XFragment, FragmentInjection
from fastapi import FastAPI, APIRouter, Depends


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
            pass
