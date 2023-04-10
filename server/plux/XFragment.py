

from fastapi import FastAPI,APIRouter
class XFragment:
    def __init__(self,app:FastAPI):
        router = APIRouter()
        self.register_router(router)
        app.include_router(router)


    def register_router(self,router:APIRouter):
        pass
