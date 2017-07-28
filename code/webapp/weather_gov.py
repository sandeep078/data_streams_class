#weather_gov.py

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find
# install with 
#    $ pip install bs4  (or pip3 install bs4)

import requests
import datetime
from bs4 import BeautifulSoup

def get_weather_page(location):
    response = requests.get("http://www.srh.noaa.gov/zipcity.php?inputstring="+str(location))
    assert(response.status_code == 200)
    return response.text

def get_weather_table_page(location):
    html = get_weather_page(location)
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())
    anchor = soup.find("a",id="3dayHist")
    link = anchor['href']
    response = requests.get(link)
    assert(response.status_code == 200)
    return response.text    

def get_weather_table(location):
    html = get_weather_table_page(location)
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())
    tables = soup.find_all("table")
    data_table = None
    data_rows = None
    for table in tables:
        rows = table.find_all("tr")
        if len(rows) > 10:
            data_table = table
            data_rows = rows
            break
    assert data_table != None
    data = []
    for row in data_rows: #[0:10]:
        items = row.find_all("td")
        if len(items) == 0:
            continue
        #print(items[0].string)
        #print(items[1].string)
        #print(items[6].string)
        #print(items[10].string)
        date = int(items[0].string)
        hhmm = items[1].string.split(":")
        hour = int(hhmm[0])
        minute = int(hhmm[1])
        now = datetime.datetime.now()
        sample_time = datetime.datetime(now.year, now.month, date, hour, minute)
        if date > now.day:
            sample_time = sample_time - datetime.timedelta(month=1)
        #print(int(sample_time.strftime("%s")))
        item = {
            "time": str(sample_time),
            "epoch": int(sample_time.strftime("%s")),
            "temp":float(items[6].string),
            "humidity":float(items[10].string.replace("%","")),
        }
        data.append(item)
    return data

if __name__ == "__main__":
    #print(get_weather_page("44281"))
    #print(get_weather_table_page("44240"))
    #print(get_weather_table("44240"))
    print(get_weather_table("Dallas,TX"))
