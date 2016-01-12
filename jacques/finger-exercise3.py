# THE TASK:
# ---------
#Write a program that asks the user to enter an integer and prints two integers,
#root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered
#by the user. If no such pair of integers exists, it should print a message to that effect.


# INITIALIZING VARIABLES
# ----------------------
root = 1
pwr = 1
found_rootpwr_pair = False


# ORIENTING THE USER
# ------------------
print "Number Games 3: Prepare to enter one (1) number"


# MAIN PROGRAM
# ------------
x = int(raw_input('Enter an integer: '))

while root**2 <= x:

	while pwr < 6 and found_rootpwr_pair == False:
		#print "DEBUG: Within the first while loop 'root' is currently: " + str(root)
		#print "DEBUG: Within the first while loop 'pwr' is currently: " + str(pwr)		
		if root**pwr == x:
			print "The number you entered has a root number of " + str(root) + ", raised to the power of " + str(pwr) + ". "
			found_rootpwr_pair = True
			#print "DEBUG: Within the nested while loop 'root' is currently: " + str(root)
			#print "DEBUG: Within the nested while loop 'pwr' is currently: " + str(pwr)
			break #NOTE: Remember that 'break' simply exits the current loop - it does not quit the entire program
		pwr += 1
	
	root += 1
	pwr = 1


if found_rootpwr_pair == False:
	print "No root / power pair exists for the given parameters."