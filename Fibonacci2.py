#(More)Efficient solution for the nth character of the Fib Sequence
import time
start_time = time.time()

#Change this to the index in the Fibonacci sequence you are interested in
nth=133000


solved = {-1:0, 0:0, 1:1}
temp=0
hold=0
def fib (i) -> int:
  if(solved.get(i)!=None):
    return solved[i]
  else:
    temp=fib(i-1)+fib(i-2)
    solved[i]=temp
  return temp

for x in range (0,nth):
  fib(x-1)
big=fib(nth+1)

print(big)
print("The length of the "+str(nth)+"th Fibonacci sequence: "+str(len(str(big))))
print("--- %s seconds ---" % (time.time() - start_time))
