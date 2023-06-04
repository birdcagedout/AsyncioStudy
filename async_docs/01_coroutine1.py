# https://docs.python.org/3/library/asyncio-task.html

# Coroutines : async def 문법으로 정의된 함수 형태
# 특히 특히 yield 기반의 coroutine과 구별하기 위해
# async 기반 coroutine을 "native coroutine"이라고 부른다.


import asyncio

async def main():
	print('Hello')
	await asyncio.sleep(1)
	print('world')


# main()                  # coroutine은 이렇게 호출해도 실행되지 않는다
asyncio.run(main())       # 이렇게 해야 실행된다
