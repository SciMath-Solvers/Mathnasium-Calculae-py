import asyncio as aio
from functools import wraps
# Decorators, cuz why not

async def aio(func):
    @wraps(func)
    async def Wrapper():
        if func == func :
            res = await aio.run(func.__name__())
            return res
    return await Wrapper()