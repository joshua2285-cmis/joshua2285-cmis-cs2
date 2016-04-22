#Time
import time
run = raw_input("Start? ")
seconds = 0
if run == "Start":
	while seconds != -1:
		print "You servived ", seconds, "Seconds of class. :D"
		time.sleep(1)
		seconds +=1


