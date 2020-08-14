import time
#IMPORTANT: matplotlib needs to be installed for this to fuction
#unless you are running this directly on Google Colab
import matplotlib.pyplot as plt
import random

x=[1,2]
y=[100,99]

start_time = time.time()

for  i in range (1,99):
    y.append(99-i)
    x.append(2+i)

#Change count to the number of sorts you want
count = 10000
for i in range (1,count):
    q=random.randint(0,99)
    w=random.randint(0,99)
    y[q],y[w]=y[w],y[q]
    if(i%30==0):
        plt.bar(x, y)
        plt.plot()
        plt.show()

print("--- %s seconds ---" % (time.time() - start_time))
