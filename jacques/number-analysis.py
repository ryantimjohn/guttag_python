largest_odd = 0
print "Number Games: Prepare to enter three (3) numbers"
x = int(raw_input("First Number: "))
y = int(raw_input("Second Number: "))
z = int(raw_input("Third Number: "))

if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
	print "None of the numbers entered are odd"
else:
        if x > y:
                largest_odd = x
        else:
                largest_odd = y
	
        if largest_odd > z:
                print "The largest odd number you entered is: ", largest_odd
        else:
                print "The largest odd number you entered is: ", z
