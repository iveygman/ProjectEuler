from itertools import permutations

# makes a list of all 0 - 9 pandigital numbers in string format
#	We drop the ones that begin with a 0 because they technically don't include all digits
#	0 through 9 exactly once
def generatePandigitals():
	# don't add one that starts with a 0
	_nums = [''.join(p) for p in permutations('0123456789')]
	nums = [n for n in _nums if n[0] != '0'];	
	return nums;
	
"""
	The problem statement is that each substring must be divisible by a prime from the
	list [2,3,5,7,11,13,17]. So what you do here is check each number as a string, parse
	it into its requisite substrings (converting them to ints as you go), then checking
	their divisibility.
	
	A few optimizations are made to simplify computation
"""
def checkSubstringDivisibility(nums):
	list = []
	for num in nums:
		subs = []
		factors = [2, 3, 5, 7, 11, 13, 17]
		ok = True
		# first optimization: skip if 4th digit not even
		if (int(num[3]) % 2 != 0):
			continue
		# second optimization: skip if 6th digit not 5 or 0
		if not (num[5] == '5' or num[5] == '0'):
			continue
		for k in xrange(1,8):
			sub = int(num[k:(k+3)])
			subs.append(sub);
		for k in range(0,len(factors)):		
			if subs[k] % factors[k] != 0:
				ok = False
				break
		if ok:
			list.append(int(num))
	
	return list
				
"""
Problem 43 Statement:

	The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of 
	the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

	Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

	d2d3d4=406 is divisible by 2
	d3d4d5=063 is divisible by 3
	d4d5d6=635 is divisible by 5
	d5d6d7=357 is divisible by 7
	d6d7d8=572 is divisible by 11
	d7d8d9=728 is divisible by 13
	d8d9d10=289 is divisible by 17
	Find the sum of all 0 to 9 pandigital numbers with this property.
"""
def doProb43(verbose=True):
	nums = generatePandigitals();
	list = checkSubstringDivisibility(nums)
	if verbose:
		print list
	print "Result: ",sum(list)