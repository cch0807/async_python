"""
코드가 비동기적으로 동작한다. -> 코드가 반드시 정의된 순서대로 동작하는것이 아니다.
"""

import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")
    return mealtime


async def main():
    result = await asyncio.gather(
        delivery("A", 3),
        delivery("B", 3),
        delivery("C", 3),
    )
    print(result)


# async def main():
#     await delivery("A", 2)
#     await delivery("B", 2)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
