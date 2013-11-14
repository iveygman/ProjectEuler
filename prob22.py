import urllib
import os.path

def getNames():
	
	names = None
	
	# check if file already exists
	exists = os.path.isfile("prob22_names.txt")
	
	# if file doesn't exist, pull it from web
	if not exists:
		urllib.urlretrieve ("http://projecteuler.net/project/names.txt", "prob22_names.txt")
	
	f = open("prob22_names.txt","r")
	s = f.read()
	f.close()
	names = s.replace('"','').split(',')	# parse into a list
	
	return names
	
def computeNameScore(name):
	score = 0
	for c in name:
		score += ord(c.upper())-ord('A')+1
	return score

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""
def doProb22():
	names = getNames()
	if names is not None:
		scoretot = 0
		names = sorted(names)
		for k in range(0,len(names)):
			scoretot += computeNameScore(names[k])*(k+1)
		print "Score total is: ",scoretot
	else:
		print "Error! Can't get names from file"
	