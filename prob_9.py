import time
start_time=time.time()
list_1=[]
for i in range(500):
    list_1.append(i)
list_2=list_1[::-1]
triplet=True
for i in list_2:
        z=i
        while triplet:
            difference=1000-z
            y=list_1[list_1.index(z)-1]
            x=list_1[difference-y]
            while triplet:
                if x+1==y or x==y:
                    break
                else:
                    if x**2+y**2==z**2:
                        print(x*y*z)
                        triplet=False
                        del list_2[0:-1]
                    else:
                        x += 1
                        y -= 1
            break

print(time.time()-start_time)
