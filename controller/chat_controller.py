from fastapi import APIRouter, Depends, Response, Request
from model.dto import ChatDTO
from service.chat_service import ChatService
from fastapi.responses import StreamingResponse


chat_router = APIRouter()

@chat_router.options("/v1/chat/completions")
def options_completions(response: Response):
    # 处理预检请求，返回允许的方法
    response.headers["Access-Control-Allow-Methods"] = "POST"
    return response

@chat_router.post("/v1/chat/completions")
def chat_completions(data: ChatDTO, service: ChatService = Depends()):
    """
    处理AI聊天请求并返回流式响应。
    :param data: 请求体数据，问题内容，上下文
    :param service: AI聊天服务
    :return: 返回流式响应，支持Server-Sent Events（SSE）
    """
    headers = {
        # 设置返回数据类型是SSE
        'Content-Type': 'text/event-stream;charset=UTF-8',
        # 保证客户端的数据是新的
        'Cache-Control': 'no-cache',
    }
    return StreamingResponse(service.chat(data), headers=headers)