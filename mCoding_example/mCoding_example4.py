# task가 완료된 후의 처리
# 각 task가 완료된 후에 리턴값을 처리할 수도 있다.
# 이때는 asyncio.wait()에서 timeout 파라미터를 주었는지 여부에 따라 처리방법이 달라진다.

# 1. timeout을 주지 않은 경우
# 	각각의 task가 완료된 후에 리턴된 값은 done에 들어가며 ==> done을 loop로 돌려서 result()로 확인 (이때 pending에는 빈 dict 들어감 = {})

# 2. timeout을 준 경우(timeout 내에  task가 끝나지 않아도 task는 종료됨)
# 	각각의 task가 완료되었다면 리턴값은 done에 들어가며
#	어느 task가 완료되기 전에 timeout되었다면 (리턴값도 당연히 없다)  ==> pending(dict임) 안에 timeout된 task의 정보가 저장된다.


import time
import asyncio


async def do_work(work: str, delay_sec: float = 1.0):
	print(f"{work} started")
	await asyncio.sleep(delay_sec)
	print(f"{work} done")
	return "*** " + work + " ***"


async def main():
	start = time.perf_counter()
	todo = ['get package', 'laundry', 'bake cake']
	delay = {'get package': 0.5, 'laundry': 1, 'bake cake': 2}


	# done에는 정상적인 리턴값이 들어가고, 
	# timeout 설정하면 timeout됐을 때 pending으로 값 들어감 (주의:TimeoutError는 발생하지 않음!!)
	# 이 경우 아직 task가 끝나지 않아서 리턴값이 없으므로 ==> InvalidStateError 발생 (asyncio.exceptions.InvalidStateError: Result is not set.)

	tasks = [asyncio.create_task(do_work(item, delay[item])) for item in todo]
	# done, pending = await asyncio.wait(tasks)								# timeout을 안 주는 경우
	done, pending = await asyncio.wait(tasks, timeout=1.2)				# timeout을 주는 경우

	for task in done:
		result = task.result()
		print(result)

	for pend in pending:
		try:
			result_pending = pend.result()
		except asyncio.exceptions.InvalidStateError:
			print("asyncio.exceptions.InvalidStateError: Result is not set.")


	end = time.perf_counter()
	print(f"it took {end - start:.2f}s")


if __name__ == '__main__':
	asyncio.run(main())
	print("__main__ 내부")


# timeout을 안 주는 경우: 결과는
# get package started
# laundry started
# bake cake started
# get package done
# laundry done
# bake cake done
# *** laundry ***
# *** get package ***
# *** bake cake ***
# it took 1.01s
# ==> 원하는 결과가 나왔다



# timeout을 주는 경우: 결과는 
# get package started
# laundry started
# bake cake started
# asyncio.exceptions.InvalidStateError: Result is not set.
# asyncio.exceptions.InvalidStateError: Result is not set.
# asyncio.exceptions.InvalidStateError: Result is not set.
# it took 0.51s