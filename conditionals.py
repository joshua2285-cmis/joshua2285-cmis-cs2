# The player had been trap inside a locked room, there is a key pad on the side of the door 
print "you are locked in a room and there are many different doors with passcode and you are trying to break free."

#import
import random

# Correct pass
def correctpass():
	correctpass = random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)
	return correctpass

# Compare
def compare():
	correctpass = correctpass()
	print correctpass
	incertcode = str(raw_input("Type the password: "))
	
	if incertcode == correctpass:
		return True

	else:
		return False

# Win or lose
def result():
	

# Main
def main():
	correctpass()
	compare()

main()
	

