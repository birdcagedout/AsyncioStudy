# asyncio.create_task(coro, *, name=None, context=None)
# 1. Wrap the coro coroutine into a Task and schedule its execution. Return the Task object.
# 2. 반드시 리턴값을 변수(reference)에 save할 것. 안 그러면 reference가 없는 것으로 간주해 garbage collecting될 수도 있다.
#	 그리고 완료된 task에 대한 reference는 지우는 것이 좋다
