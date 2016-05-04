#import
import random

thenumber = int(random.randint(0,100))
print thenumber
def guess(numberoftimes = 0):
	guessnumber = str(raw_input("next: "))
	if thenumber == guessnumber:
		print "Good job"
	
	elif thenumber > guessnumber:
		print "Too high"
		numberoftimes + 1
		guess(numberoftimes)

	elif thenumber < guessnumber:
		print "Too low"
		numberoftimes + 1
		guess(numberoftimes)

	elif numberoftimes >= 5:
		print "you fail"

guess()
	
