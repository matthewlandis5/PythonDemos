#This solves for the sin of any value from user imput

import math
import time

print("sin(x)")
imput=(float)(input("x = "))%(2*math.pi)

start_time = time.time()

sum=0
temp=0
for i in range (0,10):
  temp=((-1)**i)*((imput)**(2*i+1))/math.factorial(2*i+1)
  sum+=temp

print(sum)
print("--- %s seconds ---" % (time.time() - start_time))
