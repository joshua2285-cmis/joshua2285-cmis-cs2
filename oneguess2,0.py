#import
import random

thenumber = str(random.randint(0,100))

def guess(numberoftimes = 0):
	guessnumber = str(raw_input("next: "))
	
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

	
def main(Round = 0):
	Round += 1
	print Round

	if Round == 3:
		print "Thanks for playing."
	else:
		
		guess()
		main()
	
main()
