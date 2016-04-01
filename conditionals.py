print "you are locked in a room and there are many different doors with passcode and you are trying to break free."

#import
import random
import time



# Time
#import time
#run = raw_input("Ready? > ")
#seconds = 1
#if run == "Ready":
#	while seconds != 6:
#		print "You used ", seconds
#		time.sleep(1)
#		seconds +=1

# Main
def main():
	correctpass = random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)
	print correctpass
	incertcode = raw_input("Type the password: ")

	if incertcode == correctpass:
		print "Good Job your are free now!!!! You won!"

	else:
		print "Alarm had went off, Game over!"

	
main()

# http://stackoverflow.com/questions/18722753/trying-to-generate-a-series-of-unique-random-numbers
