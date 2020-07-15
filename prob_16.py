import time
start_time=time.time()

num=str(2**1000)
sum=0
for i in num:
    sum=sum+int(i)

print(sum)
print(time.time()-start_time)
    
