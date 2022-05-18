import asyncio
import learningkafka.consumer as consumer  # noqa: E402
import learningkafka.producer as producer  # noqa: E402


def test_simple_e2e_async():
    consume_task = consumer.consume_async()
    message = "hello world"
    result = asyncio.run(producer.send_one_async(message))
    assert result == 1

    result = asyncio.run(consume_task)
    assert result == bytes(message, "utf8")
