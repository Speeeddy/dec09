import asyncio
import time

# run two say_after co-routines concurrently

async def say_after(delay, what):  # event loops
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(say_after(2, 'hello'))
    task2 = asyncio.create_task(say_after(3, 'world'))

    print(f"started at {time.strftime('%X')}")
    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

# print(main())
asyncio.run(main())  # invoke/ run async task
