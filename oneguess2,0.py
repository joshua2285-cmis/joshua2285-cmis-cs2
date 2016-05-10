#import
import random

thenumber = int(random.randint(0,100))

def guess(numberoftimes = 0):
	guessnumber = int(raw_input("next: "))
	
	if numberoftimes == 5:
		print "you fail"

	elif thenumber == guessnumber:
		print "Good job"
	
	elif thenumber < guessnumber:
		print "Too high"
		numberoftimes += 1
		guess(numberoftimes)

	elif thenumber > guessnumber:
		print "Too low"
		numberoftimes += 1
		guess(numberoftimes)


def main(Round = 1):
	if Round == 4:
		print "Thanks for playing."
	else:
		print Round
		Round += 1
		thenumber = int(random.randint(0,100))
		guess()
		main(Round)
		
	
main()

