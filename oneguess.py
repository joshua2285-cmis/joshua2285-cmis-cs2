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
I am thinking of a number from  {} to {}.
""" .format(minnumber, maxnumber)

	guessnumber = raw_input("What do you think it is?: ")
	undernumber = random.randint(int(minnumber), int(maxnumber)) - int(guessnumber)
	overnumber = int(guessnumber) - random.randint(int(minnumber), int(maxnumber))
	
	if thenumber > guessnumber:
		print """
The target was {}.
Your guess was {}.
That's under by {}.
""" .format(thenumber, guessnumber, undernumber )
	elif thenumber < guessnumber:
		print """
The target was {}.
Your guess was {}.
That's over by {}.
""" .format(thenumber, guessnumber, overnumber)
	elif thenumber == guessnumber:
			print """
The target was {}.
Your guess was {}.
That's correct! You must be psychic!
""" .format(thenumber, guessnumber)

main()

