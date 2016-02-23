# GPA calculation
def gpacalculation(a, b, c, d, e, f, g):
	gpa = (((a + b + c + d + e + f + g) / 7.0) *4.0)/100.0
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
	x = raw_input("How many classes do you have? ")
	a = raw_input("What is your percentage for one of your classes? In whole number ")
	b = raw_input("What is your percentage for another of your classes? In whole number ")
	c = raw_input("What is your percentage for another of your classes? In whole number ")
	d = raw_input("What is your percentage for another of your classes? In whole number ")
	e = raw_input("What is your percentage for another of your classes? In whole number ")
	f = raw_input("What is your percentage for another of your classes? In whole number ")
	g = raw_input("What is your percentage for another of your classes? In whole number ")
	
	gpa = gpacalculation(int(a), int(b), int(c), int(d), int(e), int(f), int(g))
	print output(name, gpa)

main()
