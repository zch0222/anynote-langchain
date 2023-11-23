from fastapi import Depends, FastAPI
import redis


def get_redis():
    r = redis.Redis(host='localhost', port=6379, db=0)
    try:
        yield r
    finally:
        r.close()
