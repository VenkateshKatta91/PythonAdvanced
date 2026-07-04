#Normal synchronous code for API call
# from unittest import result
# import time

# def api_call():
#     time.sleep(3)  # Simulating a delay for the API call
#     return "Orders fetched successfully"

# def execute():
#     print("Executing API call...")
#     result=api_call()
#     print("Data Fetched:",result)

# execute()

#Async API Calls
import asyncio

async def api_call():
    await asyncio.sleep(3)  # Simulating a delay for the API call
    return "Orders fetched successfully"

async def execute():
    print("Executing API call...")
    result = await api_call()
    print("Data Fetched:", result)

asyncio.run(execute())