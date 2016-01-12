iters_left = 10
old_input = 0

while iters_left !=0:
	new_input = int(raw_input("Please enter an integer, %d left:"% iters_left)) 
	if new_input % 2 == 1 and new_input > old_input:
		old_input = new_input
	iters_left -= 1

if old_input == 0:
	print "No odd numbers entered."
else:
	print "%d was  the greatest odd integer entered." % old_input 
