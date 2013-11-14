def doProb1():
	threes = []
	fives = []
	# all multiples of 3 between 1 and 1000
	for k in range(1,int(1000.0/3)+1):
		threes.append(k*3)
	# all multiples of 5 between 1 and 1000
	for k in range(1,int(1000/5)):
		fives.append(k*5)
	
	# merge the two lists of multiples and remove duplicates
	tot = list(set(fives + threes))
	print sum(tot)