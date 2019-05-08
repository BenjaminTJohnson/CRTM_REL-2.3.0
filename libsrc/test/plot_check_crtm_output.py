import numpy as np
import matplotlib.pyplot as plt

f = open('data.txt', 'r')

instrument= "CrIS"
n_channels = 399 #399 for cris399_npp, 22 for atms_npp
n_layers = 92
channel_number = 398


TBa = []
Qa = []
Pressa = []
Q_Ka = []
i = 0
for line in f.readlines():
    #print(repr(line))
    #'92    1   22    273.3560    242.6359  0.6129E-28\n'
    line = line.strip()
    #'92    1   22    273.3560    242.6359  0.6129E-28'
    columns = line.split()
    #[92    1   22    273.3560    242.6359  0.6129E-28]

    Qa.append(float(columns[4])) #humidity (Q)
    TBa.append(float(columns[5])) #TB
    Q_Ka.append(float(columns[6])) #Q jacobian
    Pressa.append(float(columns[3])) #Pressure levels
    i = i + 1
f.close()

#n_channels refers to number of channels, 92 is the number of layers

Q = np.reshape(Qa,(n_channels,92))
TB = np.reshape(TBa,(n_channels,92))
Q_K = np.reshape(Q_Ka,(n_channels,92))
Press = np.reshape(Pressa,(n_channels,92))

# do some plotting, here's an example.  Modify to fit your data:
print Q_K


#example vertical plot of jacobian
plt.subplot(1,2,1)
plt.plot(Q[channel_number,0:92],Press[channel_number,0:92],'r')
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])

plt.xlabel('Humidity mass mixing ratio (Q) [g/kg]')
plt.ylabel('Vertical Pressure Levels [hPa]')
plt.title(instrument+" Ch: "+str(channel_number)+ " TB: "+str(TB[channel_number,0])+" [K]")
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(Q_K[channel_number,0:92],Press[channel_number,0:92])
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])

plt.xlabel('Humidity Jacobian [dTB/dQ]')
#plt.ylabel('Vertical Pressure Levels [hPa]')
ax.get_yaxis().set_ticklabels([])
plt.title("Jacobian")
plt.grid(True)
plt.savefig("test.png")  #macos command line "open test.png" to view.  Linux, try "display test.png" 

#plt.show()  #may not work over x11 or macos (it hung for me)



