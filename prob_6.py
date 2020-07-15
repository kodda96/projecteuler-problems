def sum_of_the_squares(num):
	sum_1 = 0
	for i in range(num+1):
		sum_1 = sum_1 + i**2
	return sum_1

def squre_of_the_sum(num):
	sum_2 = 0
	for i in range(num+1):
		sum_2 = sum_2 + i
	return sum_2**2

def difference(num):
        dif = squre_of_the_sum(num) - sum_of_the_squares(num)
        return dif

print(difference(100))

