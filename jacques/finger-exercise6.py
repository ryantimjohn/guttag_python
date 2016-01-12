# THE TASK:
# ---------
#Finger exercise: What would have to be changed to make the code in Figure
#3.4 work for finding an approximation to the cube root of both negative and
#positive numbers? (Hint: think about changing low to ensure that the answer
#lies within the region being searched.)


# MAIN PROGRAM
# ------------
print ""
x = -347
epsilon = 0.01
numGuesses = 0
low = -9999999999.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
	print 'low =', low, 'high =', high, 'ans =', ans
	numGuesses += 1
	
	if ans**3 < x:
		low = ans
	else:
		high = ans
	ans = (high + low)/2.0
print ""
print 'numGuesses =', numGuesses
print ans, 'is close to cube root of', x
print ""