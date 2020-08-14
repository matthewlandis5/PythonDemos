#Nilakantha Series: for calculating PI

import time
start_time = time.time()

solvedPi=3
temp=0
add=True

for i in range (2,20000,2):
  temp=4/(i*(i+1)*(i+2))
  if(add):
    solvedPi=solvedPi+temp
    add=False
  else:
    solvedPi=solvedPi-temp
    add=True

print("{0:.100f}".format(solvedPi))
print("--- %s seconds ---" % (time.time() - start_time))

#NOTE: This is only tested to be accurate to the first 30ish digits of PI
