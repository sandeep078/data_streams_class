// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  Serial.setTimeout(1000);
}

String sensor_value(String id) {
  if (id == "A0") {
    return String(analogRead(A0) * (5.0 / 1023.0));
  }
  if (id == "A1") {
    return String(analogRead(A1) * (5.0 / 1023.0));
  }
  if (id == "A2") {
    return String(analogRead(A2) * (5.0 / 1023.0));
  }
  if (id == "A3") {
    return String(analogRead(A3) * (5.0 / 1023.0));
  }
  if (id == "A4") {
    return String(analogRead(A4) * (5.0 / 1023.0));
  }
  if (id == "A5") {
    return String(analogRead(A5) * (5.0 / 1023.0));
  }
  return("!");
}

// the loop routine runs over and over again forever:
void loop() {
  String s = Serial.readStringUntil('\n');
  if (not s or s.equals("")) {
    Serial.println("?");
    return;
  }
  char c0 = s.charAt(0);
  char cn = s.charAt(s.length()-1);
  if (c0 != '[' or cn != ']') {
    Serial.println("!");
    Serial.println("[[[[[");
    Serial.println(s);
    Serial.println("]]]]]");
    return;
  }
  s = s.substring(1,s.length()-1);
  s.toUpperCase();
  Serial.print("[");
  Serial.print(s);
  Serial.print("=");
  Serial.print(sensor_value(s));
  Serial.println("]");
}
