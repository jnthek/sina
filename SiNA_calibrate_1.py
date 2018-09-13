import serial
import numpy as np

freq_low = 1000000
freq_up  = 10000000
points = 100
step = (freq_up-freq_low)/points
freq_cal = range(freq_low, freq_up, step)
freq_cal = np.asanyarray(freq_cal)

ser = serial.Serial('/dev/ttyUSB0',19200,timeout=1)  # open serial port
if ser.isOpen():
     print(ser.name + ' is open...')
     
print "Resolution is "+str(step/1000.0)+" kHz"

if freq_up > freq_low*2:
    print "Warning! You may see response to harmonics" 

for i in range(4):   
    ser.write(chr(50))
    ser.write(chr(50))
    s = ser.readline()
    
raw_input("Connect short and press Enter to continue...")
V_s = np.array([])
for freq in freq_cal:
    freq_send = freq/1000
    ser.write(chr(freq_send/256))
    ser.write(chr(freq_send%256))
    line = ser.readline()
    V_s = np.append(V_s, int(line[0:-2]))

raw_input("Connect open and press Enter to continue...")
V_o = np.array([])
for freq in freq_cal:
    freq_send = freq/1000
    ser.write(chr(freq_send/256))
    ser.write(chr(freq_send%256))
    line = ser.readline()
    V_o = np.append(V_o, int(line[0:-2]))

cal_coeff = 2.0/(V_o+V_s) #Needs more analysis
np.savetxt("Cal_table.txt",np.column_stack([freq_cal,cal_coeff]))


