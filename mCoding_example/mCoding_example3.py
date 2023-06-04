# 2번 예제의 결과에서 개선되지 않은 것은 task를 각각 만들어서 await를 하지 않았기 때문이다.
# 아래와 같이 고친다

import time
import asyncio


async def do_work(work: str, delay_sec: float = 1.0):
	print(f"{work} started")
	await asyncio.sleep(1)
	print(f"{work} done")


async def main():
	start = time.perf_counter()
	todo = ['get package', 'laundry', 'bake cake']

	# for item in todo:
	# 	await do_work(item)

	tasks = [asyncio.create_task(do_work(item)) for item in todo]		# for loop를 이렇게 바꿔준다 ==> 주의 create_task(이 부분에 for in까지 넣지말것)
	done, pending = await asyncio.wait(tasks)

	end = time.perf_counter()
	print(f"it took {end - start:.2f}s")


if __name__ == '__main__':
	asyncio.run(main())


# 결과는
# get package started
# laundry started
# bake cake started
# get package done
# laundry done
# bake cake done
# it took 1.01s
# ==> 원하는 결과가 나왔다