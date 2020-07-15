import time
start_time=time.time()

x=2
first_number=1
second_number=1
fibonacci_number=0

while len(str(fibonacci_number))!=1000:
    fibonacci_number=first_number+second_number
    first_number=second_number
    second_number=fibonacci_number
    x+=1
    
print(x) 
print(time.time()-start_time)
