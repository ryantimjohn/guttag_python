def findAnEven(l):
	"""Assumes l is a list of integers
	Returns the first even number in l
	Raises ValueError if l does not contain an even number"""
	
	firstEven = None
	
	for number in l:
		if number % 2 == 0:
			firstEven = number
			break
		else:
			pass
	
	if firstEven == None:
		raise ValueError
	else:
		print number
		return number

findAnEven([3,4,5,5,5,5,8])
