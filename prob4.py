from euler_utils import isPalindrome
"""
Problem description:

A palindromic number reads the same both ways. The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 x 99. Find the largest palindrome made from the product of two 3 digit numbers.

	Solves problem 4  using brute force, taking O(N^2) time. Finds all palindromes, then
	takes the biggest.
	
	Optimization: loop BACKWARD over three-digit numbers because you'll hit that palindrome earlier
"""
def doProb4():
	biggest = 0
	for x in range(999,99,-1):
		for y in range(999,99,-1):
			if isPalindrome(x*y):
				if biggest < x*y:
					biggest = x*y
	print "Biggest palindrome is",biggest