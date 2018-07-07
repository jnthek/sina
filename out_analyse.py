import numpy as np
import matplotlib.pyplot as plt

f = open("out5.txt",'r')
freq = np.array([])
amp = np.array([])
for line in f:
    line = line.strip()
    if line[0]=='F':
        freq = np.append(freq,float(line[4:]))
    else:
        amp = np.append(amp,float(line[3:]))

#plt.plot(freq[0:100],amp[0:100],label="unavg")      

#for i in range(101):
#    amp[i] = amp[i]+amp[101+i]+amp[202+i]
#    
#amp = amp/3.0
#plt.plot(freq[0:100],amp[0:100],label="avg")
plt.plot(freq,10*np.log10(amp),label="original")
plt.legend()
plt.show()
