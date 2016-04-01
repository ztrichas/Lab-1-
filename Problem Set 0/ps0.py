def sumFunction(list):
	total = 0
	for i in list:
		total = total + i
		
	return total





""" Function 0 """
#Function detects if the number is even by seeing if there is a remainder when dividing by two
def is_even(x):

	if x >= 0:
		if x % 2 >= 1: #If the remainder is greater than or equal to one 
		
			return False
		else:
			return True

	

""" Function 1 """
#Function determines the length of a number by using a counter and dividing, counting the number of times that happens
def length(x):
	
	counter = 0 
	
	while x >= 1:
		x = x / 10  
		counter += 1  

	return counter

""" Function 2"""
#Divides the number by 10 repeatedly and counts the remainders, then adds them together 
def sum_digits(x):
    sum = 0 
    while x > 0:
		sum += x % 10
		x = x / 10
    return sum


""" Function 3 """
#Takes the sum of all the lesser ints
def sum_of_lesser_ints(x):
	list = range(x)
	b = sumFunction(list)#Make own sum function #Loop and add
	return b


""" Function 4 """
#Gets the factorial of the number
def factorial(x):

	if x == 0: 
		return 1  
	else:
		x = int(x)
		list= []
	
		while x >= 1: 
			list.append(x)
			x = x -1 
	
		product = 1  
		for x in list[:len(list)]: 
			product *= x 
	
		return product 

""" Function 5 """
# Determines whether the first number is a factor of the 2nd
def is_it_a_factor(x, y):
	if x and y >= 0:
		if y % x > 0:
			return False
		else:
			return True

""" Function 6 """
# Determines whether a number is prime by dividing it by 2,3,5, and 7, which are the only things that would determine if it wasnt prime
def is_it_prime(x):
	if x == 1 or x == 0: 
		return False 
	else: 
		if int(x) % 2 == 0 and int(x) != 2: 
			return False
		if int(x) % 3 == 0 and int(x) != 3:
			return False
		if int(x) % 5 == 0 and int(x) != 5:
			return False
		if int(x) % 7 == 0 and int(x) != 7:
			return False
		else:
			return True


""" Function 7 """
#Determines whether the number is perfect by taking the number and seeing if its factors added together equal the number
def is_it_perfect(x):
	list= [] 
	list2 = []
	
	for i in range(1, x + 1): 
		if x % i == 0: 
			list.append(i) 
	if x == 0: 
		return False 
	else:
		if sumFunction(list) - x == x:
		 	return  True 
		else: 
			return False

""" Function 8 """
 
#Determines if the sum of the digits divides evenly into the number, and calls on the previous sum_digits function 
def sum_divided_by_number(x): 

	if x == 0: 
		return False 
	else:
		sum_digits_function = sum_digits(x)  
		if x % sum_digits_function == 0:
			return True
		else:
			return False 


