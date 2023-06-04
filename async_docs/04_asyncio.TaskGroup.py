# asyncio.TaskGroup 클래스를 사용하면 ==> create_task()보다 우아하게 사용할 수 있다.
# python 3.11부터 사용할 수 있다.



import time
import asyncio


async def say_after(delay, what):
	await asyncio.sleep(delay)
	print(f"{what} ----- {time.strftime('%X')}")


async def main():

	async with asyncio.TaskGroup() as tg:
		task1 = tg.create_task(say_after(1, 'hello'))
		task2 = tg.create_task(say_after(2, 'world'))
	
		print(f"started at {time.strftime('%X')}")
	
	# await를 명시적으로 부르지 않아도 된다
	# The await is implicit when the context manager exits.

	print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
