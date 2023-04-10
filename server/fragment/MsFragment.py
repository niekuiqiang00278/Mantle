from server.plux.XFragment import XFragment

from fastapi import FastAPI, APIRouter


class MsFragment(XFragment):
    def __init__(self, app: FastAPI):
        XFragment.__init__(self, app)

    def register_router(self, router: APIRouter):
        @router.post('/fff')
        async def fff():
            pass
