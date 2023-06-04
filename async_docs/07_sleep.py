# coroutine asyncio.sleep(delay, result=None)

# 1. Block for delay seconds.
# 2. If result is provided, it is returned to the caller when the coroutine completes.
# 3. sleep() always suspends the current task, allowing other tasks to run.

# Example of coroutine displaying the current date every second for 5 seconds:

import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())