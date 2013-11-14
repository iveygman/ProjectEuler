from math import sqrt

phi = (sqrt(5)+1)/2

"""
	Returns the n-th Fibonacci number as computed by Binet's formula: 
		Fib(n) = ( (phi)^n - (-phi)^-n ) / sqrt(5)
	Where phi = (1 + sqrt(5))/2
"""
def fib(n):
	global phi
	return int( ( phi ** n - (-phi) ** -n ) / sqrt(5) )