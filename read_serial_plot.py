import serial
import numpy as np
import matplotlib.pyplot as plt
#import sys
      
#freq_low = 3000000
#freq_up  = 3500000

freq_low = 3000000
freq_up  = 3500000
points = 500
step = (freq_up-freq_low)/points
freq_plot = range(freq_low, freq_up, step)
freq_plot = np.asanyarray(freq_plot)

ser = serial.Serial('/dev/ttyUSB1',19200,timeout=1)  # open serial port
if ser.isOpen():
     print(ser.name + ' is open...')
     
print "Resolution is "+str(step/1000.0)+" kHz"

if freq_up > freq_low*2:
    print "Warning! You may see response to harmonics" 

for i in range(4):   
    ser.write(chr(50))
    ser.write(chr(50))
    s = ser.readline()

ret_loss = np.array([])
#i = 0
for freq in range(freq_low, freq_up, step):
    i=i+1
    freq_send = freq/1000
    ser.write(chr(freq_send/256))
    ser.write(chr(freq_send%256))
    line = ser.readline()
    ret_loss = np.append(ret_loss, int(line[0:-2]))
#    sys.stdout.write('\r{:02d}: {}'.format(i, '#' * (i / 2)))
#    sys.stdout.flush()
ser.close() 

plt.plot(freq_plot/1e6,ret_loss)
plt.show()

