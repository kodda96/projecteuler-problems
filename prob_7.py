import time
x=time.time()
list_1=[]
list_2=[]
for i in range(2,200000):
    list_2.append(i)
for i in list_2:
    y=i
    for i in range(2,y+1):
        if i==y:
            list_1.append(y)
        elif y%i == 0:
            break
    if len(list_1)==10001:
        print (list_1[-1])
        break

print(time.time()-x)    
    
