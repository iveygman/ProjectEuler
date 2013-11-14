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
				
# actually does the problem
def doProb43(verbose=True):
	nums = generatePandigitals();
	list = checkSubstringDivisibility(nums)
	if verbose:
		print list
	print "Result: ",sum(list)

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the 
digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


Solution:
	Use itertools with the base string '0123456789' and then sort the results, taking the millionth element
"""
def doProb24():
	_nums = [''.join(p) for p in permutations('0123456789')]
	nums = sorted(_nums)
	print nums[999999]