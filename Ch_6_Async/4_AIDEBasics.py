import asyncio

async def process():
    print("First Step")
    await asyncio.sleep(2)  # Simulating a delay
    print("Second Step")

#Event Loop Begins
asyncio.run(process())