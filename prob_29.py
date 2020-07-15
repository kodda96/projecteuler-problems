import time
start_time=time.time()
myset=set()

for i in range(2,101):
    for y in range(2,101):
        number=i**y
        myset.add(number)

print(len(myset))
print(time.time()-start_time)
