import time
start_time=time.time()
x=600851475143
list=[]
for i in range(2,100000):
    if x%i==0:
        isprime=True
        d=2
        while d<i:
            remainder=i%d
            if remainder==0:
                isprime=False
            d+=1
        if isprime:
            list.append(i)

print(max(list))
print(time.time()-start_time)
