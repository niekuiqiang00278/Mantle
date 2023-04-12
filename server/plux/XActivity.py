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
        self.fragment(app)
        uvicorn.run(app,host='192.168.31.208',port=8082)

    def fragment(self, app: FastAPI):
        pass
