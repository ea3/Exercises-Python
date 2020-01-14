def lesser_of_two_evens(a,b):
	if (a % 2 ==0) and (b % 2 == 0):
		if(a < b):
			return a
		elif(b < a):
			return b
		else:
			print("The numbers are equal")
	else:
		if(a > b):
			return a
		elif(b > a):
			return b
		else:
			print("The numbers are equal")

print(lesser_of_two_evens(2, 2))





##########################   FUnction that takes a two- word 
#string and returns true if both words begin witht he same letter


def animal_crackers(text):
	str = text.split()
	#print(str[0][0])
	#print(str[1][0])
	#print(str)
	if (str[0][0] == str[1][0]):
		return True
	else:
		return False


print(animal_crackers("LevelHeaded LLama"))


###################################Given two inteers, return True if the sum of the integers is 20 or if 
#one of the integers is 20. If not, return False.

def makes_twenty(number1, number2):
	if(number1 == 20  or number2 == 20):
		print("One of the numbers is 20")
		return True
	elif(number1 + number2 == 20):
		print("The sum of the numbres is 20")
		return True
	else:
		print("Either the sum or operands were 20")
		return False


makes_twenty(2,3)
