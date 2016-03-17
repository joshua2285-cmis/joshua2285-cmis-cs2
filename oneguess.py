#Import
import random


#Main
def main():
	minnumber = int(raw_input("What is the minimum number? "))
	maxnumber = int(raw_input("What is the maximum number? "))
	thenumber = int(random.randint(minnumber, maxnumber))
	print """
I am thinking of a number from  {} to {}.
""" .format(minnumber, maxnumber)

	guessnumber = int(raw_input("What do you think it is?: "))
	wrongby = abs(thenumber - guessnumber)
	
	def findoverorunder():
		if thenumber < guessnumber:
			overorunder == "over"
		elif thenumber > guessnumber:
			overorunder == "under"
		return overorunder

	if thenumber == guessnumber:
			print """
The target was {}.
Your guess was {}.
That's correct! You must be psychic!
""" .format(thenumber, guessnumber)

	elif thenumber != guessnumber :
		print """
The target was {}.
Your guess was {}.
That's {} by {}.
""" .format(thenumber,guessnumber, overorunder,  wrongby)

main()

