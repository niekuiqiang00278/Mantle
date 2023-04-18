from functools import lru_cache
import os
class Ta:
    env = 'env'
    dev = 'dev'
    pro = 'pro'
@lru_cache()
def register_env() -> str:
    os.environ.setdefault(Ta.env, Ta.dev)
    return os.environ.get(Ta.env, Ta.dev).lower()

env = register_env()