from typing import Optional,Dict,Any
from fastapi.responses import JSONResponse
class ApiResponse(JSONResponse):
    status_code: int = 200
    result: Optional[Dict[str, Any]] = None
    code: int = 0
    msg: str = ''

    def __init__(self,
                 status_code=None,
                 code=None,
                 result=None,
                 msg=None,
                 **options):
        if status_code:
            self.status_code = status_code
        if code:
            self.code = code
        if result:
            self.result = result
        if msg:
            self.msg = msg
        super(JSONResponse, self).__init__(
            status_code=self.status_code,
            content=dict(
                status_code=self.status_code,
                code=self.code,
                data=self.result,
                msg=self.msg),
            **options)
