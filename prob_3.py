num = 600851475143
d=2
list=[]
for i in range(100000):
    if num%d==0:
        list.append(num/d)
        num = num/d
    else:
        d += 1
