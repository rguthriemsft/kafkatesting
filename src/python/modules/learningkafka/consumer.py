""" consumer """
from aiokafka import AIOKafkaConsumer
import asyncio


async def consume_async() -> str:
    """ consume """

    consumer = AIOKafkaConsumer(
        'aiopython', 'hello-world',
        bootstrap_servers='localhost:9092',
        group_id="my-group")

    # Get cluster layout and join group `my-group`
    await consumer.start()

    try:
        # Consume messages
        async for msg in consumer:
            # print("consumed: ", msg.topic, msg.partition, msg.offset,
            #      msg.key, msg.value, msg.timestamp)
            return msg.value
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()

if __name__ == "__main__":
    asyncio.run(consume_async())
