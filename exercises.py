def lesser_of_two_evens(a,b):
	if (a % 2 ==0) and (b % 2 == 0):
		return min(a,b)
	else:
		return max(a,b)

print(lesser_of_two_evens(10,20))





##########################   FUnction that takes a two- word 
#string and returns true if both words begin witht he same letter


def animal_crackers(text):
	str = text.lower().split()
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



##############Write a function that capitalizesthe first and fourth letters of a name 

def old_macdonald(name):
	first_letter = name[0].upper()
	inbetween = name[1:3]
	fourth_letter = name[3].upper()
	rest = name[4:]

	return first_letter + inbetween + fourth_letter + rest 

print(old_macdonald("macdonald"))


def master_yoda(text):
	wordlist = text.split()
	reverse_word_list = wordlist[::-1]

	return " ".join(reverse_word_list)

print(master_yoda("El amor es una magia"))


l = range(61)

print l[0:50:10]


########################
def almost_there(n):
	return (abs(100 - n) <= 10) or(abs(200 - n) <= 10)

print(almost_there(104))


############### Given a list of ints, return true if the aarray contains a 3 next to a 3 somewhere.

def has_33(num):
	for i in range(0, len(num) - 1):
		if num[i] == 3 and num[i+1] == 3:
			return True
	return False

print(has_33([1,3,3]))


######################## Given a string, return a
 #string whre for every character in the original there are three characters

def paper_doll(text):
	result = ''
 	for char in text:
 		result += char*3
 	return result


print(paper_doll("Emilio"))


#### Blackjack!
##Given 3  integers between 1 and 11, if their sum is less than or equal to 21, return their sum
##If their sum exceed 21 and there is an eleven, reduce the total sum by 10.
##Finally, if the sum(even after adjustment) exceeds 21, return "BUST"

def blackjack(a,b,c):
	if sum([a,b,c]) <= 21:
		return sum([a,b,c])
	elif 11 in [a,b,c] and sum([a,b,c]) - 10 <= 21:
		return sum([a,b,c]) - 10
	else:
		return "BUST"


print(blackjack(9,9,9))


###### Return the sum of the numbers in the array, except ignore sections
##of numbers starting with a 6 and extending to the next 9(every 6 will be 
### followed by at least one nine). Return 0 for no numbrs. 

def summer_69(arr):
	total = 0
	add = True
	for num in arr:
		while add:
			if num != 6:
				total += num
				break
			else:
				add = False

		while not add:
			if num != 9:
				break
			else:
				add = True
				break
	return total

print(summer_69([4,5,6,7,8,9]))


### Spygame. Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):

	code = [0,0,7,'x']
	print (code)

	for num in nums:
		print (code)
		if num == code[0]:
			code.pop(0)

	return len(code) == 1


print (spy_game([1,2,4,0,0,7,5]))


## Write a function that returns the number of prime number that exist up to and including the given number. 

def count_primes(number):
	#checking conditions. 

	if number < 2 :
		return 0
#####
	# 2 or greater. 
#####
###Store prime numbres. 
	primes = [2]

	##Counter going up to the input number. 
	x = 3

	while x <= number:
		for y in primes:
			if x%y == 0:
				x += 2
				break
		else:
			primes.append(x)
			x += 2

	print(primes)
	return len(primes)

print (count_primes(100))





















































