#!/usr/bin/env python
# import asyncio
import aioredis
import learningkafka.consumer as consumer  # noqa: E402
import learningkafka.producer as producer  # noqa: E402


async def test_simple_kafka_async():
    consume_task = consumer.consume_async()
    message = "hello world"
    result = await producer.send_one_async(message)
    assert result == 1

    result = await consume_task
    assert result == bytes(message, "utf8")


async def test_simple_redis_async():
    # Redis client bound to single connection (no auto reconnection).
    redis = aioredis.from_url("redis://localhost:6379")
    await redis.set("test", "value")
    val = await redis.get("test")
    print(val)
