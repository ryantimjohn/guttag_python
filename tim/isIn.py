def isIn(str1, str2):
	if str1 in str2 or str2 in str1:
		return True
	else:
		return False

string1 = raw_input("enter a string")
string2 = raw_input("enter another string")	
	
print isIn(string1, string2)