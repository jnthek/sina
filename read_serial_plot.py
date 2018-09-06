import serial
import numpy as np
import matplotlib.pyplot as plt

freq_low = 3000000
freq_up  = 3500000
step = 10000
freq_plot = range(freq_low, freq_up, step)
freq_plot = np.asanyarray(freq_plot)

ser = serial.Serial('/dev/ttyUSB1',9600,timeout=1)  # open serial port
if ser.isOpen():
     print(ser.name + ' is open...')
     
ser.write(chr(50))
ser.write(chr(50))
s = ser.readline()
ser.write(chr(50))
ser.write(chr(50))
s = ser.readline()

ret_loss = np.array([])
for freq in range(freq_low, freq_up, step):
    freq_send = freq/1000
    ser.write(chr(freq_send/256))
    ser.write(chr(freq_send%256))
    line = ser.readline()
    ret_loss = np.append(ret_loss, int(line[0:-2]))
ser.close() 

plt.plot(freq_plot/1e6,ret_loss)
plt.show()

