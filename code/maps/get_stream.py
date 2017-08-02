import requests
import json

stream_url = "https://data.sparkfun.com/output/RM44YzYqmjHqv5d1o2JQ.json"

def get_stream_data():
    response = requests.get(stream_url)
    if response.status_code != 200:
        return None
    data = json.loads(response.text)
    return data[0:1000]

if __name__ == "__main__":
   data = get_stream_data()
   print(len(data))
   print(data)
