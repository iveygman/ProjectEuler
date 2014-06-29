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

	eval('doProb'+str(prob)+'()')
	
if __name__ == "__main__":
	main()