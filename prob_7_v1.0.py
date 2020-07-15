import time
start_time=time.time()
list=[2]
value = 3
while len(list)< 10001:
    isprime = True
    for i in list:
        if value%i==0:
            value += 2
            isprime=False
            break
    if isprime:
        list.append(value)
        value += 2
    if len(list)==10001:
        print(list[-1])

print(time.time()-start_time)        
