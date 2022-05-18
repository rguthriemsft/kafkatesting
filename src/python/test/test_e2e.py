import asyncio


async def count_async():
    print("One")
    await asyncio.sleep(1)
    print("Two")

    return 1


async def gather_async():
    results = await asyncio.gather(count_async(), count_async(), count_async())

    return results[0] + results[1] + results[2]


def test_answer():

    result = asyncio.run(gather_async())
    assert result == 3
