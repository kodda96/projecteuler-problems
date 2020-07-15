import time
import math
start_time=time.time()
count=0

for i in range(3,2540160):
    num=str(i)
    sum=0
    for y in num:
        sum=sum+math.factorial(int(y))
    if sum==i:
        count=count+i

print(count)        
print(time.time()-start_time)    
