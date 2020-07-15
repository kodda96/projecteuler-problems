import math
number = 600851475143
list=[]
def prime(num):
    for i in range(2,int(math.sqrt(num)+1)):
               if num%i==0:
                   return False
    return True
                   
for i in range(2,int(math.sqrt(number)+1)):
            if number%i==0:  
               if prime(i):
                   list.append(i)

print(max(list))
