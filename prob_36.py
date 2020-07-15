import time
start_time=time.time()
sum=0

for i in range(1,1000000):
    if str(i)==str(i)[::-1]:
        binary=bin(i)[2:]
        if str(binary)==str(binary)[::-1]:
            sum=sum+i

print(sum)
print(time.time()-start_time)
