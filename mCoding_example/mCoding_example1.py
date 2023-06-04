# 출처: https://www.youtube.com/watch?v=ftmdDlwMwwQ&t=11s

import time


def do_work(work: str, delay_sec: float = 1.0):
	print(f"{work} started")
	time.sleep(delay_sec)
	print(f"{work} done")


def main():
	start = time.perf_counter()
	todo = ['get package', 'laundry', 'bake cake']

	for item in todo:
		do_work(item)

	end = time.perf_counter()
	print(f"it took {end - start:.2f}s")


if __name__ == '__main__':
	main()
		
# 결과는 
# get package started
# get package done
# laundry started
# laundry done
# bake cake started
# bake cake done
# it took 3.00s