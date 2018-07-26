import numpy as np
import matplotlib.pyplot as plt

f = open('data.txt', 'r')

TB = []

i = 0
for line in f.readlines():
    #print(repr(line))
    #'   Brightness Temperature        :  2.577742E+02\n'
    line = line.strip()
    #'   Brightness Temperature        :  2.577742E+02'
    columns = line.split()
    #   ['Brightness' 'Temperature' ':'  '2.577742E+02']
    name = columns[0]+columns[1]+columns[2] #modify this to match your data output columns
    
    TB.append(float(columns[3])) #this is a number column, append the list for each item.
    print(name, TB[i])    
    i = i + 1
    
f.close()

# do some plotting, here's an example.  Modify to fit your data:
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")  #macos command line "open test.png" to view.  Linux, try "display test.png" 

#plt.show()  #may not work over x11 or macos (it hung for me)



