#import
from math import sqrt
from math import pi
import easygui
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
def circle_area(a):
	return pi*a**2

circle_area(5)

# Volume of sphere
def sphere_volume(s):
	return (s**3) * pi * 4/3

print sphere_volume(5)

# Diameters of a sphere
def avg_volume(v1,v2):
	return (((((v1)/2)**3)*pi*4/3)+((((v2)/2)**3)*pi*4/3))/2

print avg_volume(10,20)

# Area of triangle
def area(l1,l2,l3):
	p=(l1+l2+l3) / 2
	return sqrt(p * (p - l1) * (p - l2) * (p - l3))

print area(1, 2, 2.5)

# Hello right align
def right_align(r):
	return " " * (80 - int(len(r))) + str(r)

print right_align("Hello")

# Hello center
def center(z):
	return " " * (40 - int(len(z)/2)) + str(z)

print center("Hello")

# Message Box

def msg_box(a):
	return easygui.msgbox(a)

print msg_box("Hello")
print msg_box("I eat cats!")

# call functions twice
adding01 = add(7,4) 
adding02 = add(add(add(7,8),add(6,1)),add(4,7))
subtract01 = sub(7,6)
subtract02 = sub(sub(sub(79,4),16),sub(9,3))
multiply01 = mul(7,3)
multiply02 = mul(mul(mul(mul(74,1),mul(12,756)),0),100000)
division01 = div(22,7)
division02 = div(143, 43) 
hours_from_second = hours_from_seconds(86400)
circle_area = circle_area(5)
avg_volume = avg_volume(10,20)
area = area(1, 2, 2.5)
right_align = right_align("Hello")
center = center("Hello")
msg_box01 = msg_box("Hello")
msg_box02 = msg_box("I eat cats!")


