# await를 적용할 수 있는 대상은 3가지: coroutine, Tasks, Futures

# 1. coroutine : 이 문서(https://docs.python.org/3/library/asyncio-task.html)에서는 "coroutine"을 다음 2가지로 사용한다.
#   - a coroutine function: an async def function 그 자체
#   - a coroutine object: an object returned by calling a coroutine function.
# 						    (coroutine function의 리턴값이란 뜻이 아니고, coroutine function을 그냥 호출하면 만들어지는 인스턴스 object라는 뜻이다. 아래 참고 )


import asyncio

async def nested():
    return 42

async def main():

    # 아래와 같이 호출하면 아무 것도 실행되지 않고
    # 단지, coroutine object가 만들어질 뿐이다.
    # ==> 실행되려면 coroutine object를 await 해주어야 한다.
    nested()						# <coroutine object nested at 0x000001AA76635D20>

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())
