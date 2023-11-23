from fastapi import APIRouter, Depends, Request, Response, BackgroundTasks
from model import PDFRequestDTO, ResData
from fastapi.responses import StreamingResponse

from service import RagService

rag_router = APIRouter()


@rag_router.post("/api/rag/pdf")
def pdf(pdf_request_dto: PDFRequestDTO, service: RagService = Depends()):
    headers = {
        # 设置返回数据类型是SSE
        'Content-Type': 'text/event-stream',
        # 保证客户端的数据是新的
        'Cache-Control': 'no-cache',
    }
    return StreamingResponse(service.pdf(pdf_request_dto), headers=headers)
