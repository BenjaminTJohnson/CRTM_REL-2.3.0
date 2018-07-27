import numpy as np
import matplotlib.pyplot as plt

f = open('data.txt', 'r')

TBa = []
Ta = []
Pressa = []
T_Ka = []
i = 0
for line in f.readlines():
    #print(repr(line))
    #'92    1   22    273.3560    242.6359  0.6129E-28\n'
    line = line.strip()
    #'92    1   22    273.3560    242.6359  0.6129E-28'
    columns = line.split()
    #[92    1   22    273.3560    242.6359  0.6129E-28]

    Ta.append(float(columns[4])) #temperature
    TBa.append(float(columns[5])) #TB
    T_Ka.append(float(columns[6])) #T jacobian
    Pressa.append(float(columns[3])) #T jacobian
    i = i + 1
f.close()

T = np.reshape(Ta,(22,92))
TB = np.reshape(TBa,(22,92))
T_K = np.reshape(T_Ka,(22,92))
Press = np.reshape(Pressa,(22,92))

# do some plotting, here's an example.  Modify to fit your data:
print T_K
channel_number = 21

#example vertical plot of jacobian
plt.plot(T_K[channel_number,0:92],Press[channel_number,0:92])
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])

plt.xlabel('Jacobian [TB/q]')
plt.ylabel('Vertical Pressure Levels [hPa]')
plt.title('title')
plt.grid(True)
plt.savefig("test.png")  #macos command line "open test.png" to view.  Linux, try "display test.png" 

#plt.show()  #may not work over x11 or macos (it hung for me)



