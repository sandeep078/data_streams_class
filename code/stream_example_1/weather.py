import unittest
import requests

API_KEY = "10954d4150659a315d31faf812ecc62e"

url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}"

def get_weather_data(location):
    #response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Akron,OH&APPID=10954d4150659a315d31faf812ecc62e") 
    response = requests.get(url.format(location, API_KEY)) 
    assert response.status_code == 200
    data=response.json()
    temperature = data['main']['temp'] - 270
    humidity = data['main']['humidity']
    return temperature, humidity 

class TestStringMethods(unittest.TestCase):

    def test_weather_data_call(self):
        temperature, humidity = get_weather_data("Kent,OH")
        assert 5 <= humidity <= 95
        assert -20 <= temperature <= 70

if __name__ == '__main__':
    unittest.main(verbosity=2)