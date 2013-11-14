import math
from itertools import permutations

# makes a list of all 0 - 9 pandigital numbers
def generatePandigitals():
	# don't add one that starts with a 0
	_nums = [''.join(p) for p in permutations('0123456789')]
	nums = [n for n in _nums if n[0] != '0'];
	
	return nums;
	
def checkSubstringDivisibility(nums):

	list = []
	for num in nums:
		#print "Check ",num
		subs = []
		factors = [2, 3, 5, 7, 11, 13, 17]
		ok = True
		if (int(num[3]) % 2 != 0):
			continue
		if not (num[5] == '5' or num[5] == '0'):
			continue
		for k in xrange(1,8):
			sub = int(num[k:(k+3)])
			#print sub
			subs.append(sub);
		for k in range(0,len(factors)):		
			if subs[k] % factors[k] != 0:
				#print subs[k],"not divisible by",factors[k]
				ok = False
				break
		if ok:
			list.append(int(num))
			print "Found ",num
	
	return list
		
		

def main():

	nums = generatePandigitals();
	list = checkSubstringDivisibility(nums)
	print list
	print sum(list)

if __name__ == "__main__":
	main()		