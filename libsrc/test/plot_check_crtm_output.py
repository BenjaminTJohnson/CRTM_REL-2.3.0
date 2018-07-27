import numpy as np
import matplotlib.pyplot as plt

f = open('data.txt', 'r')

TBa = []
Ta = []
T_Ka = []
i = 0
for line in f.readlines():
    #print(repr(line))
    #'92    1   22    273.3560    242.6359  0.6129E-28\n'
    line = line.strip()
    #'92    1   22    273.3560    242.6359  0.6129E-28'
    columns = line.split()
    #[92    1   22    273.3560    242.6359  0.6129E-28]

    Ta.append(float(columns[3])) #temperature
    TBa.append(float(columns[4])) #TB
    T_Ka.append(float(columns[5])) #T jacobian
    i = i + 1
f.close()

T = np.reshape(Ta,(22,92))
TB = np.reshape(TBa,(22,92))
T_K = np.reshape(T_Ka,(22,92))

# do some plotting, here's an example.  Modify to fit your data:
print T_K
channel_number = 5

#example vertical plot of jacobian
plt.semilogx(T_K[channel_number,0:92],list(reversed(range(92))))

plt.xlabel('Jacobian [TB/K]')
plt.ylabel('Vertical Levels')
plt.title('title')
plt.grid(True)
plt.savefig("test.png")  #macos command line "open test.png" to view.  Linux, try "display test.png" 

#plt.show()  #may not work over x11 or macos (it hung for me)



