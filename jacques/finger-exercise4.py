# THE TASK:
# ---------
#Finger exercise: Let 's' be a string that contains a sequence of decimal numbers
#separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints
#the sum of the numbers in 's'.


# INITIALIZING VARIABLES
# ----------------------
# setting up the s variable
s = '1.33,6.2,4.183,9.2,1.22'
total = 0.0
current = ""


# ORIENTING THE USER
# ------------------
print ""
print "The variable s is: " + str(s)
print "... processing the total of the integers within the string 's' ..."
print "------------------------------------------------------------------"
print ""


# MAIN PROGRAM
# ------------

#run through all characters in 's' and add them together

for c in s:
	if c != ',':
		current = current + c
		#print current
	else:
		total = total + float(current)
		#print "Total (so far) is: " + str(total)
		current = ""
total = total + float(current)
		

print "Final answer is below:"
print total