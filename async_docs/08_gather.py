# awaitable asyncio.gather(*aws, return_exceptions=False)

# 1. Run awaitable objects in the aws sequence concurrently.
# 2. If any awaitable in aws is a coroutine, it is automatically scheduled as a Task.


import asyncio
import threading


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        print(f"----------------------------------------------------- currently running thread: {threading.active_count()}")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(f"RESULT: {L}")

asyncio.run(main())
