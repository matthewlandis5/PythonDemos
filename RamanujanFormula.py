#Ramanujan’s Formula for Pi

import math
import time
start_time = time.time()

solved=0
j=-1
part1=0
part2=0
part3=0

for i in range (0,2):
  part1=j**i
  part2=(math.factorial(6*i))/(((math.factorial(i))**3)*math.factorial(3*i))
  part3=(13591409+(545140134*i))/(640320**(3*i))
  solved=solved+(part1*part2*part3)

PI=(53360*math.sqrt(640320))/solved
print("{0:.100f}".format(PI))
print("--- %s seconds ---" % (time.time() - start_time))

#This is a much more efficient way to calculate digits of PI
#NOTE: this has only been tested for the first 30ish digits of PI
