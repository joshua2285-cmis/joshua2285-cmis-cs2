#Main

def main():
	print """This  program will ask you for 5 integer or float values.
It will calculate the average of all valus from 0 inclusive to 10 exclusive.
It will print out whether the resulting average is even or odd."""


	firstnumber = float(raw_input("n0: "))
	if firstnumber < 0 or firstnumber > 10:
		print "{} is out of range".format(firstnumber)
		firstnumber = 0
		i1 = 0
	else: 
		i1 = 1

	secondnumber = float(raw_input("n1: "))
	if secondnumber < 0 or secondnumber > 10:
		print "{} is out of range".format(secondnumber)
		secondnumber = 0
		i2 = 0
	else: 
		i2 = 1

	thirdnumber = float(raw_input("n2: "))
	if thirdnumber < 0 or thirdnumber > 10:
		print "{} is out of range".format(thirdnumber)
		thirdnumber = 0
		i3 = 0
	else: 
		i3 = 1

	fourthnumber = float(raw_input("n3: "))
	if fourthnumber < 0 or fourthnumber > 10:
		print "{} is out of range".format(fourthnumber)
		fourthnumber = 0
		i4 = 0
	else: 
		i4 = 1

	fifthnumber = float(raw_input("n4: "))
	if fifthnumber < 0 or fifthnumber > 10:
		print "{} is out of range".format(fifthnumber)
		fifthnumber = 0
		i5 = 0
	else:
		 i5 = 1
	
	
	average = (float(firstnumber) + float(secondnumber) + float(thirdnumber) + float(fourthnumber) + float(fifthnumber)) / (i1 + i2 + i3 + i4 + i5)
	iaverage = int(average)

	if iaverage == 2: 
		ipart = "even"

	elif iaverage == 1 :
		ipart = "odd"

	elif iaverage == 3 :
		ipart = "odd"

	elif iaverage == 5 :
		ipart = "odd"

	elif iaverage == 7 :
		ipart = "odd"

	elif iaverage == 9 :
		ipart = "odd"

	elif iaverage == 4 :
		ipart = "even"

	elif iaverage == 6 :
		ipart = "even"

	elif iaverage == 8 :
		ipart = "even"

	print """ The average is {}
The integer part of the average is {}.
The integer part is {}. """.format(average, iaverage, ipart)
main()
