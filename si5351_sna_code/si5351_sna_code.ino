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
  Serial.begin(115200);
}

void loop()
{
  si5351.set_freq(freq, SI5351_CLK2);
  delay(10);
  sensorValue = analogRead(analogInPin);
 
  Serial.print("Freq"); 
  Serial.println(freq);
  Serial.print("Rv=");
  Serial.println(sensorValue);
  /*if (freq< 1100000000ULL)
    freq += 1000000ULL;
  else
    freq = 1000000000ULL;*/
    if (freq< 500000000ULL)
    freq += 1000000ULL;
  else
    freq = 300000000ULL;
   
}

