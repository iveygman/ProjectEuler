from euler_utils import *
from itertools import combinations
import os.path
import string
from subprocess import call

"""
Problem 55 Statement:

    If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

    Not all numbers produce palindromes so quickly. For example,

    349 + 943 = 1292,
    1292 + 2921 = 4213
    4213 + 3124 = 7337

    That is, 349 took three iterations to arrive at a palindrome.

    Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. 
    A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical 
    nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. 
    In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, 
    or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is 
    the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

    Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

    How many Lychrel numbers are there below ten-thousand?
"""
def isNotLychrel(num, orig=None, limit=10000, iterations=50, actionQueue = []):
    if (str(num).endswith('0')):
        return False
    palindrome = makePalindrome(num)
    if iterations<=0 or num > limit:
        return False
    n = num + int(palindrome)
    actionQueue.append( (str(num), palindrome, n) )
    if isPalindrome(str(n)):
        for a,b,c in actionQueue:
            print "{0} + {1} = {2}".format(a,b,c)
        print "{0} is a Lychrel number!".format(orig)
        return True
    else:
        return isNotLychrel(n, orig, limit, iterations-1, actionQueue)

def doProb55():
    candidates = range(1,10001) # all numbers 1 to 10000
    for candidate in candidates:
        q = []
        if not isNotLychrel(candidate, orig=candidate, limit=10000, iterations=50, actionQueue = q):
            candidates.remove(candidate) 

    print "There are {0} Lychrel numbers".format(10000-len(candidates))

"""
Problem 59 Statement:

    Each character on a computer is assigned a unique code and the preferred standard is ASCII 
    (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 
    42, and lowercase k = 107.

    A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each 
    byte with a given value, taken from a secret key. The advantage with the XOR function is that 
    using the same encryption key on the cipher text, restores the plain text; for example, 
    65 XOR 42 = 107, then 107 XOR 42 = 65.

    For unbreakable encryption, the key is the same length as the plain text message, and the key 
    is made up of random bytes. The user would keep the encrypted message and the encryption key in 
    different locations, and without both "halves", it is impossible to decrypt the message.

    Unfortunately, this method is impractical for most users, so the modified method is to use a 
    password as a key. If the password is shorter than the message, which is likely, the key is 
    repeated cyclically throughout the message. The balance for this method is using a sufficiently 
    long password key for security, but short enough to be memorable.

    Your task has been made easy, as the encryption key consists of three lower case characters. 
    Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, 
    and the knowledge that the plain text must contain common English words, decrypt the message and find the 
    sum of the ASCII values in the original text.
"""
def doProb59():
    
    if not os.path.isfile("cipher1.txt"):
        call(["wget","http://projecteuler.net/project/cipher1.txt"])
    if not os.path.isfile("cipher1.txt"):
        print "Couldn't download message file, please install wget or manually download http://projecteuler.net/project/cipher1.txt"
        return
    words = []
    with open('/usr/share/dict/words', 'r') as word_source:
        words = word_source.read().strip().split('\n')

    msg = []    
    with open('cipher1.txt', 'r') as input:
        msg = input.read().strip().split(',')
    msg = [ int(k) for k in msg ]
    keys = []
    for k in combinations(string.lowercase, 3):
        keys.append(k)
    candidates = []
    
    for count, key in enumerate(keys):
        key = [ord(k) for k in key]
        test_msg = xor_decrypt(msg, list(key))
        test_msg = [chr(k) for k in test_msg]
        test_msg = ''.join(test_msg).split(' ')
        word_count = 0
        for word in test_msg:
            if word in words:
                word_count += 1
        if word_count > 0:
            candidates.append( (word_count, test_msg) )
            print "Found {0} matches in message {1} of {2}".format(word_count, count, len(keys)) 

    print candidates        
