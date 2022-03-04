int led = 4;
int coil = 8;
int thermwrite = 6;
int thermread = A0;
double Rknown = 11000;
double Vin = 3.3;
double Vmax = 3.3;

void setup() {
  pinMode(led, OUTPUT);
  pinMode(coil, OUTPUT);
  pinMode(thermwrite, OUTPUT);
  digitalWrite(coil, 1);
  digitalWrite(thermwrite, 1);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(led, 1);
  digitalWrite(coil, 0);
  int thermValue = analogRead(thermread);
  double T = getTemp(thermValue);
  Serial.println(int(T));
  delay(3000);

  digitalWrite(led, 0);
  digitalWrite(coil, 1);
  thermValue = analogRead(thermread);
  T = getTemp(thermValue);
  Serial.println(int(T));
  delay(3000);
}

double getTemp(int thermValue){
  double R = Rknown*(((1023*Vin)/(Vmax*double(thermValue))) - 1);
  double T = 25 + log(R/10000)/log(0.96);
  return T;
}
