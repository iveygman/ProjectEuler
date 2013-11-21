import urllib
from itertools import permutations
from euler_utils import findAllDivisors,isAbundant,fib
import os.path

def getNames():
	
	names = None
	
	# check if file already exists
	exists = os.path.isfile("prob22_names.txt")
	
	# if file doesn't exist, pull it from web
	if not exists:
		urllib.urlretrieve ("http://projecteuler.net/project/names.txt", "prob22_names.txt")
	
	f = open("prob22_names.txt","r")
	s = f.read()
	f.close()
	names = s.replace('"','').split(',')	# parse into a list
	
	return names
	
def computeNameScore(name):
	score = 0
	for c in name:
		score += ord(c.upper())-ord('A')+1
	return score

"""
Problem Statement:
	Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand 
	first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
	multiply this value by its alphabetical position in the list to obtain a name score.

	For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
	is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

	What is the total of all the name scores in the file?
	
Solution:
	Pretty straightforward: read and parse all the names into a list, compute their scores and sum the total
	
"""
def doProb22():
	names = getNames()
	if names is not None:
		scoretot = 0
		names = sorted(names)
		for k in range(0,len(names)):
			scoretot += computeNameScore(names[k])*(k+1)
		print "Score total is: ",scoretot
	else:
		print "Error! Can't get names from file"
		

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
Problem Statement:
	A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
	For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

	A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

	As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two 
	abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as 
	the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known 
	that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

	Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
	
Solution:
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
	

"""
Problem 24 Statement:
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