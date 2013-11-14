from math import sqrt

phi = (sqrt(5)+1)/2

"""
	Checks if input integer or string is a palindrome, code pulled from http://stackoverflow.com/a/18959976/760318
"""
def isPalindrome(n):
	string = str(n)
	for i,char in enumerate(string):
		if char != string[-i-1]:
			return False
	return True

"""
	Pulled from http://stackoverflow.com/a/16996439/760318
	
	Returns all prime factors for n
"""
def prime_factors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

"""
	Returns the n-th Fibonacci number as computed by Binet's formula: 
		Fib(n) = ( (phi)^n - (-phi)^-n ) / sqrt(5)
	Where phi = (1 + sqrt(5))/2
"""
def fib(n):
	global phi
	return int( ( phi ** n - (-phi) ** -n ) / sqrt(5) )