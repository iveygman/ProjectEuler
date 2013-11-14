"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
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