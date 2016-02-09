# THE TASK:
# ---------
#Finger exercise: Write a function isIn that accepts two strings as arguments
#and returns True if either string occurs anywhere in the other, and False
#otherwise. Hint: you might want to use the built-in str operation in.



#ORIENTING THE USER
#------------------
print ""
print "Defining variable: isIn"


# MAIN PROGRAM
# ------------
def isIn (x, y):
#if the full string in x appears within y OR 
#the full string in y appears within x

	if str(x) in y or str(y) in x:
		print True
		return True		
	else:
		print False
		return False

	
#ORIENTING THE USER
#------------------	
print ""
print "variable definied."
print ""
print "Please enter two 'strings' to be allocated within the nely definied variable"
print "----------------------------------------------------------------------------"
user_input1 = str(raw_input("Enter 'string' 1: "))
user_input2 = str(raw_input("Enter 'string' 2: "))
print ""
isIn(user_input1,user_input2)
print ""