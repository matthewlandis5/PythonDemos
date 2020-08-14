import time
start_time = time.time()

#Modify fibIndex to the desired index in the Fibonacci sequence
fibIndex = 72000
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

for x in range (0,fibIndex):
  fib(x-1)
  
print(str(fibIndex)+"th position: "+str(fib(fibIndex)))
print("--- %s seconds ---" % (time.time() - start_time))
