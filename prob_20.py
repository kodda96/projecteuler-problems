import time
start_time=time.time()
number=100
product=1
x=0
while number!=1:
    product=product*number
    number-=1
sum=str(product)
for i in sum:
    x=x+int(i)

print(x)
print(time.time()-start_time)
