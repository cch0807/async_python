import asyncio
import time

# # task가 1개이므로 동기 프로그래밍과 크게 다르지 않다.
# async def main():
#     print('start')
#     await asyncio.sleep(1)
#     print('end')

# start = time.time()
# asyncio.run(main())
# end = time.time()
# print(end - start)

# start
# end
# 1.0051159858703613

# 동기
# def sync_task_1():
#     print('sync_task_1 시작')
#     print('sync_task_1 3초 대기')
#     time.sleep(3)
#     print('sync_task_1 종료')

# def sync_task_2():
#     print('sync_task_2 시작')
#     print('sync_task_2 3초 대기')
#     time.sleep(3)
#     print('sync_task_2 종료')

# start = time.time()
# sync_task_1()
# sync_task_2()
# end = time.time()
# print(end-start)

# 비동기
# asyncio를 쓰면 더 빠르게 처리되어야 하는데 시간이 동일하게 걸림.
# await 코루틴함수() 같은 방식으로 나열하면 코루틴을 호출하는 것이지 다음 태스크를 실행하도록 예약하는 의미가 아님.
# 여러 코루틴을 동시에 실행하여 원하는 동작을 하기 위해선 아래와 같이 create_task()로 등록해야 한다.
async def async_task_1():
    print("sync_task_1 시작")
    print("sync_task_1 3초 대기")
    await asyncio.sleep(3)
    print("sync_task_1 종료")


async def async_task_2():
    print("sync_task_2 시작")
    print("sync_task_2 3초 대기")
    await asyncio.sleep(3)
    print("sync_task_2 종료")


async def main():
    start = time.time()
    # await sync_task_1()
    # await sync_task_2()
    task1 = asyncio.create_task(async_task_1())
    task2 = asyncio.create_task(async_task_2())
    await task1
    await task2

    end = time.time()
    print(end - start)


# 메인 함수 실행
# asyncio.run(main())


async def factorial(name, number):
    f = 1
    if number == 4:
        raise ValueError("error")
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # 동시에 3개를 예약
    result = await asyncio.gather(
        factorial("A", 2), factorial("B", 3), factorial("C", 4), return_exceptions=True
    )
    # 또는
    # result = await asyncio.gather(
    #     *[factorial("A", 2), factorial("B", 3), factorial("C", 4)]
    # )
    print(result)


# asyncio.run(main())

# 시간 제한 (asnycio.wait_for())


async def eternity():
    await asyncio.sleep(4)
    print("safe!")


async def main():
    try:
        # 대기 시간이 1초가 넘어가면 에러처리
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print("timeout!")


# asyncio.run(main())

# awaitable
# await 표현식에서 사용할 수 있는 객체를 awaitable 객체라고 한다.
# 이러한 객체는 코루틴(coroutine), 테스크(task), 퓨처(future)가 있다.
