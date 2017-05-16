from __future__ import division # Only importing division from __future__ module instead of complete module
import math # math is a module which contains a set of functions, this imports complete module
import cmath # complex numbers mathematics module

print "Hello World"
print 2 + 2
print 53762 + 235253
print 1/2
print 5/2
print 5/2.0
print 5//2.0 # double slash // always performs integer division
print 4 * 5
print 5 % 2 # modulus
print 2 ** 3 # exponential
print -3 ** 2
print (-3) ** 2
print 1987163987163981639186L * 198763981726391826L + 23 # Long integers should end with L to denote them as long than normal integers

x = 2 # x is variable
print x * 3

abc = 1 # valid
a12_ = 4 # valid
_ab = 6 # valid
# ab$ = 10 # invalid
# 8ab = 11 # invalid

age = input("What is your age:"); # Reading user input, can use raw_input also
print age

print pow(2, 3) # power function
print abs(-3) # Absolute function
print round(2.3494, 2) # Round function

print math.floor(32.9) # floor is a function defined in math module
print int(math.floor(32.9)) # type casting float to int

print math.sqrt(1.0)
print cmath.sqrt(-1)
print (1+3j) * (2+4j)

print "I'm Khan"
print 'I said "do not come"'
# print 'I'm Khan' # error, can not include single colon with in a string which is surrounded by single colon
print 'I\'m Khan' # back slash used to display single colon
print "I said \"do not come\""

temp = 45
print "Today's temperature is " + `temp` + " degrees"

print '''This is a very long string.
It continues here.
And it's not over yet.
"Hello, world!"
Still here.''' # long string

print 'C:\nice\folder' # simple string, back slash characters have special meaning.
print r'C:\nice\folder' # raw string, reads as it is
