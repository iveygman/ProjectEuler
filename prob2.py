from euler_utils import fib

"""
	Using Binet's formula to compute all even-valued Fibonacci numbers until you exceed
	4 million and sum the result
"""
def doProb2():
	lim = 4e6
	
	nums = []
	n = 1
	while True:
		num =  fib(n)
		if (num <= lim):
			if num % 2 == 0:
				nums.append(num)
		else:
			break;
		n += 1
	
	print sum(nums)
	