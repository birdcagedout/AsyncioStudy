# async 함수를 호출하면 그 함수가 실행되는 것이 아니라 coroutine을 리턴한다
# await 하면 실행흐름을 멈추고(if necessary) 해당 라인이 끝날 때까지 기다린다

# <문제점 개선>
# 아래와 같이 async 형태로 바꾸고 난 후
# 3가지 작업이 각각 끝날 때까지 각각 1초씩 기다리지 말고
# 시작, 시작, 시작 하고 나서 ==> 1초를 다같이 기다리는 방식으로 바꾸어 보자

import time
import asyncio


async def do_work(work: str, delay_sec: float = 1.0):			# async로 바꾼다
	print(f"{work} started")
	await asyncio.sleep(1)										# asyncio.sleep()으로 바꾸고 + await 
	print(f"{work} done")


async def main():												# async로 바꾼다
	start = time.perf_counter()
	todo = ['get package', 'laundry', 'bake cake']

	for item in todo:
		await do_work(item)										# await 해준다

	end = time.perf_counter()
	print(f"it took {end - start:.2f}s")


if __name__ == '__main__':
	asyncio.run(main())											# 그냥 main()에서 바꿔준다


# 결과는
# get package started
# get package done
# laundry started
# laundry done
# bake cake started
# bake cake done
# it took 3.02s
# ==> 하나도 나아지지 않았다 왜 이럴까