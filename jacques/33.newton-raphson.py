# THE TASK:
# ---------
#Finger exercise: Add some code to the implementation of Newton-Raphson that
#keeps track of the number of iterations used to find the root. Use that code as
#part of a program that compares the efficiency of Newton-Raphson and bisection
#search. (You should discover that Newton-Raphson is more efficient.)


# INITIALIZING VARIABLES
# ----------------------
epsilon = 0.01


#ORIENTING THE USER
#------------------
print ""
print "            Showdown!: Bisection vs the Newton-Raphson Method"
print "-- Which method can find the square root of a positive integer faster? --"
print "-------------------------------------------------------------------------"
print ""
evaluation_num = int(raw_input("Enter A Positive Number: "))
print ""

# MAIN PROGRAM
# ------------

#Newton-Raphson Method for approximating the square root of a number
print "NEWTON-RAPHSON METHOD:"
print "----------------------"
guess = evaluation_num/2.0
NewtonRaphsonGuesses = 0
while abs(guess*guess - evaluation_num) >= epsilon:
	guess = guess - (((guess**2) - evaluation_num)/(2*guess))
	NewtonRaphsonGuesses += 1
print 'ANSWER: The square root of', evaluation_num, 'is about', guess
print '--> NOTE: [it took %d tries to find the answer using the Newton-Raphson Method]' % (NewtonRaphsonGuesses)
print ""

print "BISECTION METHOD:"
print "-----------------"
#Bisection Method for finding the square root of a number
BisectionGuesses = 0
low = 0.0
high = max(1.0, evaluation_num)
ans = (high + low)/2.0
while abs(ans**2 - evaluation_num) >= epsilon:
	print 'low =', low, 'high =', high, 'ans =', ans
	BisectionGuesses += 1
	if ans**2 < evaluation_num:
		low = ans
	else:
		high = ans
	ans = (high + low)/2.0
print 'ANSWER: %d is close to square root of %d' % (ans, evaluation_num)
print '--> NOTE: [it took %d tries to find the answer using the Bisection Method]' % (BisectionGuesses)


print ""
if NewtonRaphsonGuesses < BisectionGuesses:
	print "* The Newton-Raphson method is faster!"
elif  NewtonRaphsonGuesses == BisectionGuesses:
	print "* The two methods (Newton-Raphson and Bisection) are equivalent!"
elif BisectionGuesses < NewtonRaphsonGuesses:
	print "* The Bisection method is faster!"
	
print ""