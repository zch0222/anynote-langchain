import redis


def get_redis_pool() -> redis.Redis:
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    return redis.Redis(connection_pool=pool)

