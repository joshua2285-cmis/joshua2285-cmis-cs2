#def countdown (n):
	#if n<= 0:
	#	print "blastoff!"

	#else:
		#print n
		#countdown(n-1)


#def countdown_from_to(start, stop):
	
	#if start >= stop:
	#	print "done"
	#else:
	#	print start
	#	countdown_from_to(start+1,stop)
	#	
#countdown_from_to(0,99)

		
#def adder2(running_total = 0):
#	print "The running total is {}.".format(running_total)
#	number = raw_input("Next Number: ")
#	if number != "":
#		running_total += float(number)
#		adder2(running_total) 
#	else:
#		print "The sum is {}.".format(running_total)
#adder2()


def biggest(bignum = -float('inf')):
	number_1 = raw_input("Next Number: ")
	if number_1 == "":
		print "The biggest number is {}.".format(bignum)

	elif float(number_1) < float(bignum):
		biggest(bignum)

	elif float(number_1) > float(bignum):
		bignum = number_1
		biggest(bignum)

biggest()

