from math import sqrt
from operator import mul
from collections import Counter

phi = (sqrt(5)+1)/2

"""
    Returns the product of every element in some_list
"""
def prod(some_list):
    return reduce(lambda x, y: x * y, some_list)

"""
    returns the most common element in the list.
    optionally, can return the 2nd, 3rd, 4th, etc most common
"""
def mode(some_list,commonality=1):
    l = Counter(some_list)
    return l.most_common(commonality)[-1]

"""
    Tests whether or not a number is prime. If it's in the list, it's already prime.
    Otherwise, check if it's prime the long way ONCE, then add it to the list
"""
def isPrime(num):

    inf = open("primes.txt","r")
    s = inf.read()
    inf.close()
    primes = [ ss for ss in s.replace('\n',',').split(',') if len(ss)>0 ]

    if num in primes:   return True
    
    # otherwise check if prime the long way
    lim = int(sqrt(num))+2
    for k in range(2,lim):
        if num % k == 0:
            return False
    
    primes.append(num)
    out = open("primes.txt","w")
    for n in primes:
        out.write(str(n)+'\n')
    out.close()
    
    return True

def generateSpiral(dim):
    if dim % 2 == 0 or dim < 3:
        print "Error, generateSpiral() must take an odd-numbered dimension 3 or greater"
        return None
    spiral = [[None for x in xrange(dim)] for x in xrange(dim)] 
    
    x = int(dim/2)  # initial x and y
    y = x           
    n = 1
    
    spiral[x][y] = n
    x

"""
    Returns the Collatz sequence for n
"""
def collatz(n):
    if n <= 0:
        return None
    else:
        seq = []
        while n > 1:
            seq.append(n)
            if (n%2):   n = 3*n+1
            else:       n /= 2
        return seq

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
    Finds all proper divisors of n, where a proper divisor of n is k such that n % k == 0
    
    Restricted to positive n for now
"""
def findAllDivisors(n):

    if not (n > 1):
        return None

    divs = [1]
    
    if n > 2:
        for k in range(2,n):
            if n % k == 0:
                if k not in divs:
                    divs.append(k)
        
    
    return sorted(divs)

"""
    Returns true if and only if the input number's divisors sum to a value larger than itself
    
    Tested only on positive integers
"""
def isAbundant(num):
    if num <= 0:    return None
    divisors = findAllDivisors(num)
    return sum(divisors) > num

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