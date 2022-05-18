""" producer """
import asyncio
from aiokafka import AIOKafkaProducer


async def send_one_async(message: str) -> int:
    """ async send """
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9092')

    # Get cluster layout and initial topic/partition leadership information
    await producer.start()

    try:
        # Produce message
        await producer.send_and_wait(
            "aiopython",
            bytes(message, "utf8"),
            b"key1")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()
    return 1

if __name__ == "__main__":
    asyncio.run(send_one_async("hello"))
