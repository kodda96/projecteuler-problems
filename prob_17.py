import time
start_time=time.time()
sum=0
single={1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
double={11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
tens={10:3,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6}

for i in range(1,1000):
    number=str(i)
    if len(number)<2:
        sum=sum+single[i]
    elif len(number)==2 and number[-1]=='0':
        sum=sum+tens[i]
    elif i<20:
        sum=sum+double[i]
    elif len(number)<3:
        sum=sum+(tens[int(number[0]+'0')]+single[int(number[-1])])
    elif number[1:3]=='00':
        sum=sum+(single[int(number[0])]+7)
    elif number[-1]=='0':
        sum=sum+(single[int(number[0])]+10+tens[int(number[1:3])])
    elif number[1]=='0':
        sum=sum+(single[int(number[0])]+10+single[int(number[0])])
    elif int(number[1:3]) in double:
             sum=sum+(single[int(number[0])]+10+double[int(number[1:3])])
    else:
        sum=sum+(single[int(number[0])]+10+tens[int(number[1]+'0')]+single[int(number[-1])])

print(sum+11)
print(time.time()-start_time)
        
        
    

        
