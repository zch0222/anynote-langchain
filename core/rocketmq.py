import json

from rocketmq.client import Producer, Message
from core.config import ROCKETMQ_NAMESERVER_ADDRESS
from core.logger import get_logger


def get_producer() -> Producer:
    producer = Producer('anynote-langchain')
    producer.set_name_server_address(ROCKETMQ_NAMESERVER_ADDRESS)
    return producer

def send_message(topic: str, tags: str, body: str):
    log = get_logger()
    log.info(json.dumps({'topic': topic, 'tags': tags, 'body': body}))
    producer = get_producer()
    producer.start()
    try:
        msg = Message(topic)
        msg.set_tags(tags)
        msg.set_body(body)
        ret = producer.send_sync(msg)
        log.info(f"rocketmq sent {ret.status} {ret.msg_id} {ret.offset}")
    finally:
        producer.shutdown()