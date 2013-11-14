import sys
from prob1 import *
from prob2 import *
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
	elif prob == 43:
		doProb43()
	else:
		print "Unknown problem"
	
if __name__ == "__main__":
	main()