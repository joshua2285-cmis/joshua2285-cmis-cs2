#while 1==1:
#	print "01",



#x = 1
#while x != -1:
#	print x
#	x*= 856342333452354353245243523452452345224535652347237684567756

#def countup():
#	x = 1
#	while x!= 100:
#		print x
#		x+=1

#countup()

#def countdown():
#	x = 100
#	while x!= 0:
#		print x
#		x-=1

#countdown()

#def counting():
#	x = float(raw_input("The Number: "))
#	while x < 0:
#		print x
#		x +=1
#	while x > 0:
#		print x
#		x -=1
#counting()



#def countfrom2(x,y):
	
#	while x < y:
#		print x
#		x +=1
#	while y < x:
#		print x
#		x -=1
#countfrom2(20,12)

#def sumOfOdds(n):
#	sum = 0
#	if n>0:
#		while n > 0:
#			if n%2 ==1:
#				sum+= n
#			n -= 1
#	elif n<0:
#		while n<0:
#			if n%2 ==1:
#				sum += n
#			n+=1
#		return sum
#print sumOfOdds(10)


def grid(w,h):
	while h !=0:
		while w!= 0:
			print ".",
			w-=1
		h-=1
		
grid(10,10)

