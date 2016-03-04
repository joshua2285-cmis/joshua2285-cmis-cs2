#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#	assignment operator

#wrong
#
#2 3pts) Write a technical definition for 'function'
#	 A function is a named sequence of statements that performs a computation. 
#
#
#3 1pt) What does the keyword "return" do?
#	The result of a function. If a function call is used as an expression, the return value is the value of the expression.
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: String - ("Hi","How are you?") 
#	2: tuple - ("a", 24)
#	3:boolean - (True, False)
#	4:integer - (1,2)
#	5:floating point - (0.1, 2.3)
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#	A function definition specifies the name of a new function and the sequence of statements that execute when the function is called. calling a function is to asignent things to it.
#
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: input - you incert a string or a float
#	2: calculation - The computer runs thru it
#	3: output - The computer give something in return
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

#import
from math import sqrt
from math import pi

# calculation of radius
# a = pi * r**2

#1 pt for header line
#3 pt for correct formula    -1
#1 pt for return value
#1 pt for parameter name
#1 pt for function name

def radius(A1):
	c1 = sqrt(float(A1)/pi)
	return c1

def radius(A2):
	c2 = sqrt(float(A2)/pi)
	return c2

def radius(A3):
	c3 = sqrt(float(A3)/pi)
	return c3
# Output

#1pt for header line
#1pt for parameter names
#1pt for return value
#1pt for correct output format
#3pt for correct use of format function

def output(c1, c2, c3, t):
	return """
Circle	Diameter
c1	{}
c2	{}
c3	{}
Totals	{}
""" .format(c1, c2, c3, t)

# Main 

#1pt header line
#1pt getting input
#1pt converting input
#1pt for calling output function
#2pt for correct diameter formula
#1pt for variable names

def main():
	A1 = raw_input("Area of c1: ")
	A2 = raw_input("Area of c2: ")
	A3 = raw_input("Area of c3: ")
	c1 = radius(A1)
	c2 = radius(A2)
	c3 = radius(A3)
	t = float(c1) + float(c2) + float(c3)
	print output(c1, c2, c3, t)

main()

#1pt explanatory comments
#1pt code format

