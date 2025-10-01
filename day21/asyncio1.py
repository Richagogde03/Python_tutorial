import asyncio
# Event Loop


# basic
# couroutine function
# async def main():
#     print("Start of main couroutine")

# # main() -> couroutine object
# # main()

# # run the main couroutine
# asyncio.run(main())


# 1, event loop
# Define a coroutine that simulates a time-consuming task
# async def fetch_data(delay):
#     print("fetching data...")
#     # simulates an i/o operation with a sleep
#     await asyncio.sleep(delay)
#     print(("Data fetched"))
#     return {"data": "Some data"}


# # defining another coroutine that calls the first coroutine
# async def main():
#     print("Start of main coroutine")
#     # coroutine object
#     task = fetch_data(2)
#     result = await task
#     print(f"Received result: {result}")
#     print("End of main couroutine")

# asyncio.run(main())


# 2, couroutine
async def fetch_data(delay, id):
    print("fetching data... id", id)
    await asyncio.sleep(delay)
    print("Data fetched, id:", id)
    return {"data": "Some data", "id": id}


async def main():
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    result1 = await task1
    print(f"Received result : {result1}")

    result2 = await task2
    print(f"Received result : {result2}")


asyncio.run(main())
