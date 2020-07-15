list_1=[]
for i in range(1,21):
    list_1.append(i)
x=20
y=1
z=0
while True:
    while x%list_1[z]==0:
        z += 1
        if z==20:
            print(x)
            break 
    y += 1
    x=20*y
    if z==20:
        break
    else:
        z=0
