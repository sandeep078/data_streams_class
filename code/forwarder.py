import serial, time

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
 
time.sleep(3)
clock = time.time()
while True:
   temp = get_value(arduino,"TEMP")
   humidity = get_value(arduino,"HUMIDITY")
   print(temp, humidity)
   while time.time() < clock + 15.0:
       time.sleep(0.5)
   clock = clock + 15.0
