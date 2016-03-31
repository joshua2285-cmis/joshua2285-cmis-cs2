#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) 4 == 4 True
#b) 5 == 6 False
#c) 7 == 0 False
#
#2) What does 'return' do?
# It gives you back the value of what the function did.
#
#
#
#3) What are 2 ways indentation is important in python code?
#a) It tells the computer when the function begins and when it ends.
#b) Indentation of the statements makes the structure apparent.
#
#

#PART 2: Reading
#Type the values for 9 of the 12 of the variables below.
#
#problem1_a) -36
#problem1_b) square root of -3
#problem1_c) 0
#problem1_d) -5
#
#problem2_a) True
#problem2_b) True
#problem2_c) False
#problem2_d) True
#
#problem3_a) 0.3
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5
#
#problem4_a) 7
#problem4_b) 5
#problem4_c) 0.125
#problem4_d) 5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

# Processing function
def processing(a,b,c):
	if int(a) > int(b) and int(a) > int(c) :
		result = int(a)
	elif b > a and b > c :
		result = b
	elif c > a and c > b :
		result = c
	else:
		 result = x
	return result
# Output function
def output():
	if result == int(result) :
		print "The largest number was {}.".format(result)
	else: 
		print "You didn't follow directions "
	output()

# Main function
def main():
	print "Type in 3 different numbers (decimals are OK)"
	a = raw_input("A: ")
	b = raw_input("B: ")
	c = raw_input("B: ")

	processing(a, b, c)



main()



