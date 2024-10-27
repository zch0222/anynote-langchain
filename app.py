from fastapi import FastAPI, HTTPException
from core.config import HOST, TOKEN
from starlette.requests import Request
from starlette.responses import JSONResponse
from model.vo import ResData
from core.logger import get_logger
app = FastAPI()

# 鉴权
@app.middleware("http")
async def http_middleware(request: Request, call_next):
    # response = Response("Internal server error", status_code=500)
    if request.method == "OPTIONS":
        response = await call_next(request)
        return response
    try:
        token = request.headers["Authorization"]
        print(token)
        print(token.split()[-1])
        if token.split()[-1] != TOKEN:
            raise HTTPException(status_code=401, detail="Invalid token")
    except KeyError:
        raise HTTPException(status_code=401, detail="Missing token")

    # 继续处理请求
    response = await call_next(request)
    return response

# 全局异常处理
@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger = get_logger()
    logger.exception("An error occurred while processing request")

    # 检查异常是否为HTTPException
    if isinstance(exc, HTTPException):
        # 如果是HTTPException，返回异常指定的状态码
        return JSONResponse(
            status_code=exc.status_code,
            content=ResData.error(exc.detail)
        )
    # 对于非HTTPException异常，返回500内部服务器错误
    return JSONResponse(
        status_code=500,
        content=ResData.error("An internal server error occurred")
    )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="app:app", host=HOST, port=8000, workers=4)