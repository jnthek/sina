import serial
import numpy as np
import matplotlib.pyplot as plt

ser = serial.Serial('/dev/ttyUSB1',9600,timeout=1)  # open serial port
if ser.isOpen():
     print(ser.name + ' is open...')
     
ser.write(chr(50))
ser.write(chr(50))
s = ser.readline()
print s

ret_loss = np.array([])

freq_low = 3000000
freq_up  = 4000000
step = 10000
for freq in range(freq_low, freq_up, step):
    freq_send = freq/1000
    ser.write(chr(freq_send/256))
    ser.write(chr(freq_send%256))
    line = ser.readline()
    print line
    ret_loss = np.append(ret_loss, line)
ser.close() 

plt.plot(ret_loss)
plt.show()

