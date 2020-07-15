import time
start_time=time.time()
starting_number=2
num=2
length=1
list_1=[]
list_2=[]
while starting_number<1000000:
    num=starting_number
    while num!=1:
        if num%2==0:
            num=num/2
            length+=1
        else:
            num=(3*num)+1
            length+=1
    list_1.append(length)
    list_2.append(starting_number)
    starting_number+=1
print(list_2[list_1.index(max(list))])
print(start_time-time.time())
