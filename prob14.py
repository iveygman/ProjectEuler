from euler_utils import collatz

def doProb14():
	longest = 0
	num = 1000000
	for n in range(1000000,0,-1):
		l = len(collatz(n))
		if (longest < l):
			longest = l
			num = n
	print "Longest Collatz sequence under 1 million is",longest,"from",num