from fastapi import FastAPI, APIRouter, params
from typing import Optional, Sequence


def FragmentInjection(prefix: str, dependencies: Optional[Sequence[params.Depends]]):
    def back(cls):
        cls.prefix = prefix
        cls.dependencies = dependencies
        return cls

    return back


class XFragment:
    prefix: str
    dependencies: Optional[Sequence[params.Depends]]

    def __init__(self, app: FastAPI):
        router = APIRouter(
            prefix=self.prefix,
            dependencies=self.dependencies
        )
        self.register_router(router)
        app.include_router(router)

    def register_router(self, router: APIRouter):
        pass
