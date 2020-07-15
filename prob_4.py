list_1=[]
list_2=[]
for i in range(100,1000):
    list_1.append(i)
for i in range(100000,1000000):
    if str(i)==str(i)[::-1]:
        list_2.append(i)
list_2=list_2[::-1]
x=0
y=0
while list_2[y]/list_1[x] not in list_1:
        x += 1
        if list_1[x]==list_1[-1]:
            y += 1
            x=0
print(list_2[y])            
