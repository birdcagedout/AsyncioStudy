# await를 적용할 수 있는 대상은 3가지: coroutine, Tasks, Futures

# 2. Task : asyncio.create_task(코루틴)으로 호출하면 
# 			==> 1. 코루틴이 Task로 포장되고(coroutine is wrapped into a task)
# 			==> 2. 코루틴은 곧 자동실행되도록 스케줄된다.(the coroutine is automatically scheduled to run soon)

# 실험: 아래에서 await task를 주석처리 하고 실행해보자: 주석처리해도 "Inside nested"는 출력된다. ==> automatically scheduled to run

import asyncio

async def nested():
    print("Inside nested")
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())
