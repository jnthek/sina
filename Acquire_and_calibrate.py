import serial
import numpy as np
import matplotlib.pyplot as plt

#freq_low = 1000000
#freq_up  = 10000000
#points = 100
#step = (freq_up-freq_low)/points
#freq_plot = range(freq_low, freq_up, step)
#freq_plot = np.asanyarray(freq_plot)

freq_cal = np.loadtxt("Cal_table.txt",usecols=[0])
cal_coeff = np.loadtxt("Cal_table.txt",usecols=[1])
freq_cal = freq_cal
step = freq_cal[1] - freq_cal[0]   
freq_low = freq_cal[0]
freq_high = freq_cal[-1]

ser = serial.Serial('/dev/ttyUSB0',19200,timeout=1)  # open serial port
if ser.isOpen():
     print(ser.name + ' is open...')

print "Resolution is "+str(step/1000.0)+" kHz"

if freq_high > freq_low*2:
    print "Warning! You may see response to harmonics" 

for i in range(4):   
    ser.write(chr(50))
    ser.write(chr(50))
    s = ser.readline()
    
raw_input("Connect the network and press Enter to continue...")
V_r = np.array([])
for freq in freq_cal:
#    i=i+1
    freq_send = int(freq/1000)
    ser.write(chr(freq_send/256))
    ser.write(chr(freq_send%256))
    line = ser.readline()
    V_r = np.append(V_r, int(line[0:-2]))
#    sys.stdout.write('\r{:02d}: {}'.format(i, '#' * (i / 2)))
#    sys.stdout.flush()
ser.close() 

ret_loss = V_r*cal_coeff #Needs more analysis

plt.figure()
plt.plot(freq_cal/1e6,ret_loss)
plt.xlabel("Freq (MHz)")
plt.ylabel("Reflection Coefficient")
plt.grid()
plt.show()

