#find the cube root of a perfect cube
x = int(raw_input("Enter an integer, we'll figure out if it has a perfect cube:"))
ans = 0
while ans**3 < abs(x):
	ans = ans +1
if ans ** 3 != abs(x):
	print x, 'is not a perfect cube'
else:
	if x < 0:
		ans = -ans
	print 'Cube root of', x,'is', ans
