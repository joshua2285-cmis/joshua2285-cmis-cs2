# GPA calculation
def gpacalculation(class01,class02,class03,class04,class05,class06,class07 ):
	gpa = (((class01,class02,class03,class04,class05,class06,class07) / 7.0) *4.0)/100.0
	return gpa

# output
def output(name, gpa):
	return """
Hey there!{}!
your GPA is {}.
""" .format(name, gpa)

# Main
def main():
	name = raw_input("What is your name?: ")
	numberofclasses = raw_input("How many classes do you have? ")
	class01 = raw_input("What is your percentage for one of your classes? In whole number ")
	class02 = raw_input("What is your percentage for another of your classes? In whole number ")
	class03 = raw_input("What is your percentage for another of your classes? In whole number ")
	class04 = raw_input("What is your percentage for another of your classes? In whole number ")
	class05 = raw_input("What is your percentage for another of your classes? In whole number ")
	class06 = raw_input("What is your percentage for another of your classes? In whole number ")
	class07 = raw_input("What is your percentage for another of your classes? In whole number ")
	
	gpa = gpacalculation(int(class01), int(class02), int(class03), int(class04), int(class05), int(class06), int(class07))
	print output(name, gpa)

main()
