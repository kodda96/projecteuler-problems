import math
import time

start_time=time.time()
sum = 2
def isprime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num==2:
            return True
        elif num%i==0:
            return False
    return True
                   
for i in range(2,2000000):
    if isprime(i):
        sum += i
print(sum)
print(time.time() - start_time)
