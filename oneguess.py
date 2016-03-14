#Import
import random

# The random number
def thenumber(minnumber, maxnumber):
	return random(minnumber, maxnumber)

#Main
def main():
	minnumber = raw_input("What is the minimum number? ")
	maxnumber = raw_input("What is the maximum number? ")

	print """
I am thinking of a number from  {} to {}
""" .format(minnumber, maxnumber)

	guessnumber = raw_input("What do you think it is?: ")


	

#Main()

