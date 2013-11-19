"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two 
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as 
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known 
that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from euler_utils import findAllDivisors,isAbundant

"""
	Find all abundant numbers less than the limit and return them in a list
"""
def findAllAbundantNums(limit=28123):
	
	nums = []
	# we're given that 12 is the lower limit
	for k in range(12,limit+1):
		if isAbundant(k):
			if (k not in nums):
				nums.append(k)
	return nums

"""
	Find every abundant number under 28123, storing those numbers in a list
	Then compute every possible sum of two numbers within said list and put them in a
	list with only unique elements. 
	Finally, iterate through all numbers 1 to 28123. Any number not in the above list is summed
"""
def doProb23():
	nums = findAllAbundantNums()
	print "Abundant numbers:",nums
	sums = []
	for a in nums:
		for b in nums:
			sums.append(a+b)
			
	unique_sums = list(set(sums))
	not_in_list = []
	for k in range(1,28123):
		if k not in unique_sums:
			not_in_list.append(k)
	print "Sums to",sum(not_in_list)