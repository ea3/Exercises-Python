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


