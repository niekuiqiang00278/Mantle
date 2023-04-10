from fastapi import FastAPI, APIRouter


class XActivity:
    def __init__(self):
        app = FastAPI()
        self.fragment(app)

    def fragment(self, app: FastAPI):
        pass
