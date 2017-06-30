import serial, time

arduino = serial.Serial('/dev/cu.usbmodem1421', 9600, timeout=2.0)
time.sleep(1)
text = "[A0]\n"
bytes = text.encode("latin-1")
arduino.write(bytes)
while True:
    bytes = arduino.readline()
    if bytes:
        text = bytes.decode("utf-8").strip()
        print(text)
    text = "[A0]\n"
    bytes = text.encode("latin-1")
    arduino.write(bytes)
		#print(data.rstrip('\n') #strip out the new lines for now
		# (better to do .read() in the long run for this reason

