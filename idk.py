#Time
import time
run = raw_input("Start? ")
seconds = 1
if run == "Start":
	while seconds != 0:
		print "In T minuse ", seconds, "Seconds "
		time.sleep(1)
		seconds +=1

	if seconds <= 0:
		 print "Boom!"
