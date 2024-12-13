

from service.rag_service import RagService
from core.redis_server import RedisServer
from constants.redis_channel_constants import RAG_TASK_CHANNEL
from core.logger import get_logger

if __name__ == '__main__':
    # rag_service = RagService()
    # rag_service.rag("https://anynote.obs.cn-east-3.myhuaweicloud.com:443/anynote_Shanghai_one/doc/5450d9f3330d43a19d97d07f634f32d9.pdf",
    #                 "MySQL索引注意事项")
    logger = get_logger()
    for msg in RedisServer().subscribe(f"{RAG_TASK_CHANNEL}:6816781c-c092-43eb-afe6-fe4f946424c9"):
        logger.info(msg)
