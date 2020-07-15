import time
import math
start = time.time()
x = 1
factors = 0
triangle = True

while triangle:
    num = int(x*(x+1)/2)
    if num > 500:
        for i in range(1,int(math.sqrt(num))+1):
            if num%i==0:
                factors += 2
    if factors > 500:
        print(num)
        print(time.time() - start)
        triangle = False
    else:
        x += 1
        factors = 0
    
