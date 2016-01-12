# THE TASK:
# ---------
#Finger exercise: Write a program that asks the user to input 10 integers, and
#then prints the largest odd number that was entered. If no odd number was
#entered, it should print a message to that effect.


# INITIALIZING VARIABLES
# ----------------------
#keeps track of the number of entries made for the while loop
numbers_entered = 0
#for aesthetic purposes with the display during the raw_input prompt
raw_counter = 1
#placeholder for the current number being worked on
current_num = 1
#how many even numbers have been encountered
totaleven = 0
#placeholder for the current largest odd number encountered
largest_odd = 0


# ORIENTING THE USER
# ------------------
print "Number Games 2: Prepare to enter ten (10) different numbers"


# MAIN PROGRAM
# ------------
#begin the while loop
while (numbers_entered < 10):
	current_num = int(raw_input("Enter Number " + str(raw_counter) + ": "))
	raw_counter += 1 
		
	if current_num % 2 == 0:
		totaleven += 1
	else:
		if largest_odd > current_num:
			largest_odd = largest_odd
		else:
			largest_odd = current_num
		
	numbers_entered += 1
	
if totaleven == 10:
	print "None of the numbers entered are odd"
else:
	print "The largest odd number is: ", largest_odd
