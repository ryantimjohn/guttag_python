x = int(raw_input("Please enter an integer, we'll find a root, power combination:"))
root = 1
found = False
while root**2 <= abs(x):
	root += 1
	pwr = 2
	while root ** pwr <= x:
		if root ** pwr == x:
			found = True
			break
		else:
			print "root = ", root, "pwr = ", pwr
			pwr += 1
	if found:
		break

if found:
	print "The root is %d and the power is %d" % (root, pwr)
else:
	print "No root power pair exists."