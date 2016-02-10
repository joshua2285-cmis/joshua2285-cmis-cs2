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
import math
def circle_area(a):
	return math.pi*a**2

circle_area(5)

# Volume of sphere
import math
def sphere_volume(s):
	return (s**3)*math.pi*(4/3)

print sphere_volume(5)
