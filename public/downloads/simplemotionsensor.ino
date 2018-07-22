void setup() {
  pinMode(7, INPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, digitalRead(7));
}


