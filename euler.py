import sys
from math import factorial
from euler_utils import *
from prob00x import *
from prob01x import *
from prob02x import *
from prob03x import *
from prob04x import *
from prob05x import *
from prob06x import *
from prob07x import *
from prob08x import *
from prob09x import *

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
	elif prob == 3:
		print max(prime_factors(600851475143))
	elif prob == 4:
		doProb4()
	elif prob == 8:
		doProb8()
	elif prob == 14:
		doProb14()
	elif prob == 20:
		p = factorial(100)
		pp=[int(n) for n in list(str(p))]
		print "Sum is ",sum(pp)
	elif prob == 22:
		doProb22()
	elif prob == 23:
		doProb23()
	elif prob == 24:
		doProb24()
	elif prob == 43:
		doProb43()
	else:
		print "Unknown problem"
	
if __name__ == "__main__":
	main()