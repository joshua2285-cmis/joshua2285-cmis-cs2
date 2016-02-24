#import
from math import sqrt
from math import pi
# Adding funcion
def add(a,b):
	return a+b

add(7,4)
add(add(add(7,8),add(6,1)),add(4,7))

# subtraction function
def sub(a,b):
	return a-b

sub(7,6)
sub(sub(sub(79,4),16),sub(9,3))

# Multiplcation function
def mul(a,b):
	return a*b

mul(7,3)
mul(mul(mul(mul(74,1),mul(12,756)),0),100000)

# Division
def div(a,b):
	return float(a)/b

div(22,7)
div(143, 43)

# Seconds to Hours
def hours_from_seconds(x):
	return x/3600

hours_from_seconds(86400)

# Area of a circle
def circle_area(r):
	return pi*(r**2)

circle_area(5)

# Volume of sphere
def sphere_volume(s):
	return (s**3) * pi * 4/3

sphere_volume(5)

# Average volume of sphere
def avg_volume(v1,v2):
	
	return (sphere_volume(v1) + sphere_volume(v2)) /2
	#return (((((v1)/2)**3)*pi*4/3)+((((v2)/2)**3)*pi*4/3))/2

print avg_volume(10,20)

# Area of triangle
def area(l1,l2,l3):
	p=(l1+l2+l3) / 2
	return sqrt(p * (p - l1) * (p - l2) * (p - l3))

area(1, 2, 2.5)

# Hello right align
def right_align(r):
	return " " * (80 - int(len(r))) + str(r)

right_align("Hello")

# Hello center
def center(z):
	return " " * (40 - int(len(z)/2)) + str(z)

center("Hello")

# Message Box

def msg_box(a):
	y = "--" + "-"*len(a) + "--"
	return"""
+{}+
|  {}  |
+{}+""".format(y, a, y)

msg_box("Hello")
msg_box("I eat cats!")

# call functions twice
adding01 = add(1,2) 
adding02 = add(add(add(1,18),add(1,2)),add(5,2))
subtract01 = sub(4,2)
subtract02 = sub(sub(sub(65,2),43),sub(44,21))
multiply01 = mul(4,6)
multiply02 = mul(mul(mul(mul(21,4),mul(3,5)),1),1240)
division01 = div(1,1)
division02 = div(142123, 43) 
hours_from_second01 = hours_from_seconds(5000)
hours_from_second02 = hours_from_seconds(1)
circle_area01 = circle_area(10)
circle_area02 = circle_area(20)
avg_volume01 = avg_volume(2,5)
avg_volume02 = avg_volume(8,1)
area01 = area(4, 7, 5)
area02 = area(6, 8, 9)
right_align01 = right_align("My name is Joshua")
right_align02 = right_align("I love food!!!")
center01 = center(">.<")
center02 = center(":P")
msg_box01 = msg_box("Welcome!!!!")
msg_box02 = msg_box("How are you?")

#Out Put
print msg_box(str(adding01))
print msg_box(str(adding02))
print msg_box(str(subtract01))
print msg_box(str(subtract02))
print msg_box(str(multiply01))
print msg_box(str(multiply02))
print msg_box(str(division01))
print msg_box(str(division02))
print msg_box(str(hours_from_second01))
print msg_box(str(hours_from_second02))
print msg_box(str(avg_volume01))
print msg_box(str(avg_volume02))
print msg_box(str(area01))
print msg_box(str(area02))
print msg_box(str(right_align01))
print msg_box(str(right_align02))
print msg_box(str(center01))
print msg_box(str(center02))


