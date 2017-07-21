import serial, time
import requests

DELAY = 15

arduino = serial.Serial('/dev/cu.usbmodem1421', 9600, timeout=2.0)

def get_value(arduino, value):
    text = "[" + value + "]\n"
    bytes = text.encode("latin-1")
    print("Writing " + text)
    arduino.write(bytes)
    while True:
        bytes = arduino.readline() 
        text = bytes.decode("utf-8").strip()
        if text != "?":
            text = text.replace("[","")
            text = text.replace("]","")
            text = text.replace(value,"")
            text = text.replace("=","")
            return float(text)
 
def post_to_stream(stream,
                   userid, city, state, 
                   lat, lon, 
                   temp, humidity, light, 
                   outdoors):
    url = "http://drdelozier.pythonanywhere.com/stream/store/"
    payload = {
        'userid': str(userid),
        'city': str(city),
        'state': str(state),
        'lat': str(lat),
        'lon': str(lon),
        'temp': str(temp),
        'light': str(light),
        'outdoors': str(outdoors),
    }
    response = requests.get(url + stream, params=payload)
    print(response.status_code)
    print(response.url)
    print(response.text)

time.sleep(3)
clock = time.time()
while True:
   temp = get_value(arduino,"TEMP")
   humidity = get_value(arduino,"HUMIDITY")
   print(temp, humidity)

   post_to_stream("beta", "gdelozie", "kent", "OH", 
                   0.001, 0.002, temp, humidity, 0, 0)
   
   while time.time() < clock + DELAY:
       time.sleep(0.5)
   clock = clock + DELAY 
