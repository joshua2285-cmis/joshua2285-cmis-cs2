#import
import random


def guess(numberoftimes = 1):
	guessnumber = int(raw_input("next: "))
	thenumber = game(Round = 5)
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
	
def game(Round = 1):
	if Round == 5:
		thenumber = int(random.randint(0,100))
		return thenumber
	if Round == 4:
		print "Thanks for playing."
	else:
		print Round
		
		Round += 1
		guess()
		game(Round)


def main():
	game()	
	

	
main()

