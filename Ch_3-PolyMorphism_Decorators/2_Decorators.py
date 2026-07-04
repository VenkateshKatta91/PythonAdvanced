from urllib import response


def fetch_data(url:str,path:str):

    return f"Fetching data from {url} and saving to {path}"
response=fetch_data("https://api.example.com/data","/tmp/data.json")
print(response)