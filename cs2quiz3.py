#Section 1: Terminology
# 1) What is a recursive function?
#	A function which would call it self.
#
#
# 2) What happens if there is no base case defined in a recursive function?
#	The recursive funcion would go on forever.
#
#
# 3) What is the first thing to consider when designing a recursive function?
#	When would the recursive funciton end, and set a base case accordly.
#
#
# 4) How do we put data into a function call?
#	define
#
# 
# 5) How do we get data out of a function call?
#	return
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 2
#a2 = 6
#a3 = -1

#b1 = 2
#b2 = 
#b3 =

#c1 =
#c2 =
#c3 =

#d1 =
#d2 =
#d3 =

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.


def compare(numoftimes = 0, oddnum = 0):
	
	thenumber = raw_input("Next: ")
#Recurtion
	if thenumber != "":
		numoftimes += 1
		oddnum += float(thenumber)
		compare(numoftimes, oddnum)
# Base case
	else:
		print oddnum
		avr = (float(oddnum) / float(numoftimes))
		print avr
compare()



