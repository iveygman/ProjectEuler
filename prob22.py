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
	