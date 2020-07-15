import time
start_time=time.time()
import math
count=1
value = 3
while count < 10001:
    isprime = True
    for i in range(2,int(math.sqrt(value)+1)):
        if value%i==0:
            value += 2
            isprime=False
            break
    if isprime:
        value += 2
        count += 1
    if count==10001:
        print(value-2)

print(time.time()-start_time)        
