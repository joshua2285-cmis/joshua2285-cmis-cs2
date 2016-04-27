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

def adder():
	runtotal = 0.0
	Next_num = float(raw_input("Next Number: "))
	if Next_num != "":
		runtotal += Next_num
		print total
		adder()
		
adder()

 
