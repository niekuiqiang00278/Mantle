from fastapi import FastAPI, APIRouter
import uvicorn
from starlette.middleware.cors import CORSMiddleware
class XActivity:
    def __init__(self):
        app = FastAPI()
        app.add_middleware(
            CORSMiddleware,
            allow_origins=['*', ],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
        self.bis()
        self.rpc()
        self.fragment(app)
        uvicorn.run(app,host='127.0.0.1',port=8082)

    def rpc(self):
        pass

    def bis(self):
        pass

    def fragment(self, app: FastAPI):
        pass
