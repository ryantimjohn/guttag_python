#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0
k = float(raw_input("Give us a number to approximate the square root of: "))
if k < 0.0 :
	print "Negative numbers don't have square roots, dummy."
else:
	epsilon = float(raw_input("How close do you want to get to the answer? Write a decimal number: "))
	num_guesses = 1
	guess = k/2.0
	while abs(guess*guess - k) >= epsilon:
		num_guesses += 1
		guess = guess - (((guess**2)- k)/(2*guess))
	print "We guessed", num_guesses, "times and came up with",\
			guess, "as our best guess for the square root of", k
			

