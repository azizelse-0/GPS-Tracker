#include <SoftwareSerial.h>
#include <TinyGPS++.h>
SoftwareSerial gpsSerial(6,5);
TinyGPSPlus gps;

void setup(){
  Serial.begin(9600);
  gpsSerial.begin(9600);
}
void loop(){
  while(gpsSerial.available()){
    char c = gpsSerial.read();
    Serial.print(c);
}
}
