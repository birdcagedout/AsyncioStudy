# asyncio.create_task(실행할 코루틴)으로 코루틴을 async로 실행할 수도 있다.
# 주의: create_task() 한다고 바로 실행되는 것이 아니다. await task 해줘야 실행된다.



import time
import asyncio


async def say_after(delay, what):
	await asyncio.sleep(delay)
	print(f"{what} ----- {time.strftime('%X')}")


async def main():
	task1 = asyncio.create_task(		# 주의: 이때 task1이 실행되는 것이 아니다
		say_after(1, 'hello')
	)

	task2 = asyncio.create_task(		# 주의: 이때 task2가 실행되는 것이 아니다
		say_after(2, 'world')
	)

	print(f"started at {time.strftime('%X')}")

	# Wait until both tasks are completed (should take around 2 seconds.)
	await task1					# 이때 task1 실행됨
	await task2					# 이때 task2 실행됨

	print(f"finished at {time.strftime('%X')}")

asyncio.run(main())