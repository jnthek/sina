#include "si5351.h"
#include "Wire.h"

const int analogInPin = A0;

Si5351 si5351(0x62);
unsigned long freq;
unsigned long calfreq = 0ULL; //-7579900ULL; //calibration done with Hantek DSO
int sensorValue = 0;  

void setup()
{
  si5351.init(SI5351_CRYSTAL_LOAD_10PF,25000000, calfreq);
  freq = 360000000ULL;
  Serial.begin(9600);
}

void loop()
{ 
 Serial.flush();
 while(Serial.available()<2)
    {
       //do nothing
    }
  byte b1=Serial.read();
  byte b2=Serial.read();
  freq=(b1*256+b2)*100ULL*1000ULL;
  si5351.set_freq(freq, SI5351_CLK2);
  delay(100);
  sensorValue = analogRead(analogInPin);
  Serial.println(sensorValue);
  Serial.flush();

}

