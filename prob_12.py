import time
start = time.time()
x = 1
list=[]
triangle = True

while triangle:
    num = int(x*(x+1)/2)
    if num > 500:
        for i in range(1,num+1):
            if i not in list:
                if num%i==0:
                    list.append(i)
                    list.append(num/i)
            else:
                break
    if len(list) > 500:
        print(num)
        print(time.time() - start)
        triangle = False
    else:
        x += 1
        del list[:]
    
