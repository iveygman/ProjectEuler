import sys
from math import factorial
from euler_utils import *
from prob1 import *
from prob2 import *
from prob4 import *
from prob14 import *
from prob22 import *
from prob43 import *

def main():

	argc = len(sys.argv)
	prob = 0
	if (argc > 1):
		prob = int(sys.argv[1])
	else:
		prob = raw_input("Enter problem number: ")
	
	if prob == 1:
		doProb1()
	elif prob == 2:
		doProb2()
	"""
	The prime factors of 13195 are 5, 7, 13 and 29.

	What is the largest prime factor of the number 600851475143 ?
	"""
	elif prob == 3:
		print max(prime_factors(600851475143))
	elif prob == 4:
		doProb4()
	elif prob == 14:
		doProb14()
	"""
	n! means n × (n − 1) × ... × 3 × 2 × 1

	For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
	and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

	Find the sum of the digits in the number 100!
	"""
	elif prob == 20:
		p = factorial(100)
		pp=[int(n) for n in list(str(p))]
		print "Sum is ",sum(pp)
	elif prob == 22:
		doProb22()
	elif prob == 24:
		doProb24()
	elif prob == 43:
		doProb43()
	else:
		print "Unknown problem"
	
if __name__ == "__main__":
	main()