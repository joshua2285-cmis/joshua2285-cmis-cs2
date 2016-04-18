#Main

def main():
	print """This  program will ask you for 5 integer or float values.
It will calculate the average of all valus from 0 inclusive to 10 exclusive.
It will print out whether the resulting average is even or odd."""


	firstnumber = float(raw_input("n0: "))
	if firstnumber < 0 or firstnumber > 10:
		print "{} is out of range".format(firstnumber)
	secondnumber = float(raw_input("n1: "))
	if secondnumber < 0 or secondnumber > 10:
		print "{} is out of range".format(secondnumber)
	thirdnumber = float(raw_input("n2: "))
	if thirdnumber < 0 or thirdnumber > 10:
		print "{} is out of range".format(thirdnumber)
	fourthnumber = float(raw_input("n3: "))
	if fourthnumber < 0 or fourthnumber > 10:
		print "{} is out of range".format(fourthnumber)
	fifthnumber = float(raw_input("n4: "))
	if fifthnumber < 0 or fifthnumber > 10:
		print "{} is out of range".format(fifthnumber)

	
	average = (float(firstnumber) + float(secondnumber) + float(thirdnumber) + float(fourthnumber) + float(fifthnumber)) / 5
	iaverage = round(average,0)	
	if iaverage == 1 or 3 or 5 or 7 or 9:
		ipart = "odd"
	elif iaverage == 2 or 4 or 6 or 8 : 
		ipart = "even"	

	print """ The average is {}
The integer part of the average is {}.
The integer part is {}. """.format(average, iaverage, ipart)
main()
