import asyncio

async def api_call(url:str):
    print("Fetching data from:", url)
    await asyncio.sleep(3)  # Simulating a delay for the API call
    return f"{url} data fetched successfully"

# async def execute():
#     print("Executing API call...")
#     result = await api_call("orders")
#     print("Data Fetched:", result)

# asyncio.run(execute())

async def main():

    #Creating Tasks with Gather
    # tasks=asyncio.gather(
    #     api_call("https://api1.com""),
    #     api_call("https://api2.com""),
    #     api_call("https://api3.com"")
    # )
    tasks=[api_call(url) for url in ["https://api1.com", "https://api2.com", "https://api3.com"]]
    results=await asyncio.gather(*tasks)
    
asyncio.run(main())