from fastapi import APIRouter, Depends, Request, BackgroundTasks
from model.dto import AudioTranscriptionDTO
from model.dto.whisper_run_dto import WhisperRunDTO
from model.vo import ResData
from service.whisper_service import WhisperService
import uuid
from fastapi.responses import StreamingResponse

whisper_router = APIRouter()
@whisper_router.post("/v1/audio/transcriptions")
def transcriptions(request: Request, data: AudioTranscriptionDTO, service: WhisperService = Depends()):
    task_id = uuid.uuid4().__str__()
    headers = {
        # 设置返回数据类型是SSE
        'Content-Type': 'text/event-stream;charset=UTF-8',
        # 保证客户端的数据是新的
        'Cache-Control': 'no-cache',
    }
    return StreamingResponse(service.transcriptions(data, task_id), headers=headers)





@whisper_router.post("/api/whisper/submit")
async def whisper_submit(request: Request, background_tasks: BackgroundTasks, data: WhisperRunDTO, service: WhisperService = Depends()):
    background_tasks.add_task(service.do_whisper_task, data, data.taskId)
    res = await service.submit_whisper_task(data)
    return ResData.success({
        "taskId": data.taskId
    })