import asyncio
import concurrent.futures
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

# 코루틴
# 코루틴은 awaitable 객체이므로 다른 코루틴에서 호출할 수 있다.


async def nested():
    print(87)


async def main():
    # 코루틴 함수를 await을 안붙이고 호출하면 호출되지 않음
    # 모루틴은 생성이 되지만 await하지 않음 -> 그래서 아무것도 실행 X
    nested()

    # nested() 함수가 동시에 실행되도록 예약
    task = asyncio.create_task(nested())

    # 87 반환됨
    await nested()

    # task 변수를 취소하거나 완료될때까지 대기
    await task


# asyncio.run(main())

# 위에서 코루틴이란 용어는 코루틴 함수와 코루틴 객체라는 두 의미를 내포하는 것을 알 수 있다.
# 코루틴 함수 - async def ~~ 로 정의된 함수
# 코루틴 객체: 코루틴 함수를 호출하고 반환되는 객체

# 퓨처(future)
# 퓨처는 비동기 연산의 최종 결과를 나타내는 저수준 awaitable 객체이다.
# 현재까지 asyncio를 사용하는데 퓨처 객체를 어디서 사용해야 되는지 정확하게 이해가 되지 않는다.
# asyncio와 퓨처를 사용하는 좋은 예는 loop.run_in_executor() 이다.

def blocking_io():
    