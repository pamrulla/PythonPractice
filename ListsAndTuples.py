# You can chane a list but you can not change a tuple.
# Indexing - from zero to upwards
greetings = "Hello"
print greetings[0] # First letter 'H'

print greetings[-1] # Last leter 'o'

# TODO
# Write a program to print out a date,  given year, month and day as numbers
# Example
# Input:
# Year: 1974
# Month (1-12): 8
# Day (1-31): 16
# Output:
# August 16th, 1974

# Slicing - access a range of values
# Require two indices, frist index denotes from where start slicing - inclusive
# second index denotes upto which to slice - exclusive
tag = '<a href="http://www.python.org">Python web site</a>'
print tag[9:30] # prints 'http://www.python.org'
print tag[32:-4] # prints 'Python web site' 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers[3:6] # [4,5,6]
print numbers[0:1] # [1]

print numbers[:3] # prints first three [1,2,3]
print numbers[-3:] # prints last three [8,9,10]
print numbers[:] # pints all [1,2,3,4,5,6,7,8,9,10]

# TODO
# Write a program to Split up a URL of the form http://www.something.com
# Example
# Input:
# Please enter the URL: http://www.python.org
# Output:
# Domain name: python

# Step size
# For slicing we can include a third parameter which denotes step size, which means it displays only the numbers which matches step size.
print numbers[0:10:2] # prints [1,3,5,7,9]
print numbers[3:6:3] # prints [4]

# step size can be negatvie - extracts from end
print numbers[8:3:-1] # prints [9,8,7,6,5]
print numbers[10:0:-2] # prints [10,8,6,4,2]
print numbers[0:10:-2] # prints []
print numbers[::-2] # prints [10, 8, 6, 4, 2]
print numbers[5::-2] # prints [6, 4, 2]
print numbers[:5:-2] # prints [10,8]

# Concantenating Sequences - using + operator you can concatenate sequences of same type
print [1,2,3,4] + [5,6,7,8] # prints [1,2,3,4,5,6,7,8]

# Multiplication - Multiplying a sequence by a number x creates a new sequence where the original sequence is repeated x times
print 'python' * 5 # prints 'pythonpythonpythonpythonpython'
print [42] * 10 # prints [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]

# Empty list initialization with nothing
sequence = [None] * 10
print sequence # prints [None, None, None, None, None, None, None, None, None, None]

# TODO
# Write a program to Prints a sentence in a centered "box" of correct width
# Example
# Input:
# Sentence: He's a very naughty boy!
# Output:
#                       +——————————————————————————+
#                       |                          |
#                       | He's a very naughty boy! |
#                       |                          |
#                       +——————————————————————————+

# Membership
# To check check whether an element is present in a sequence or not.
# Use in operator 
permissions = 'rw'
print 'w' in permissions # prints True
print 'x' in permissions # Prints False

users = ['mlh', 'foo', 'bar']
print raw_input('Enter your user name: ') in users

subject = '$$$ Get rich now!!! $$$'
print '$$$' in subject # prints True

numbers = [100, 34, 678]
print len(numbers) # prints lentgh of sequence 3
print max(numbers) # prints maximum value in sequence 678
print min(numbers) # prints minimum value in sequence 34

# Only for Lists

# The list Function - splits sequence in to a list
print list("Hello") # prints ['H', 'e', 'l', 'l', 'o']

# Changing list
x = [1, 1, 1]
x[1] = 2
print x # prints [1, 2, 1]

# Deleting Elements - use del operator
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print names # prints ['Alice', 'Beth', 'Dee-Dee', 'Earl']

# Assingning Slices
name = list('Perl')
name[2:] = list('ar') # changes rl to er
print name # pints ['P', 'e', 'a', 'r']

# replace with a slice with list whose length is different
name = list('Perl')
name[1:] = list('ython')
print name # pints ['P', 'y', 't', 'h', 'o', 'n']

# can be used to insert without removing any elements
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print numbers # prints [1, 2, 3, 4, 5]

# can be used to delete a slice
numbers[1:4] = []
print numbers # prints [1,5]

# append
lst = [1, 2, 3]
lst.append(4)
print lst # prints [1, 2, 3, 4]

# count - counts the occurrences of an element in a list
print ['to', 'be', 'or', 'not', 'to', 'be'].count('to') # prints 2
x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print x.count(1) # pritns 2
print x.count([1, 2]) # prints 1

#extend
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print a # prints [1, 2, 3, 4, 5, 6]

# index - used to search for the index of an element
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
knights.index('who') # prints 4
# it throws exception if element is not present in list

# insert
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print numbers # prints [1, 2, 3, 'four', 5, 6, 7]

# pop The pop method removes an element (by default, the last one) from the list and returns it
x = [1, 2, 3]
print x.pop() # prints 3
print x # prints [1, 2, 3]
print x.pop(0)  # pints 1
print x # prints [2]

#remove - The remove method is used to remove the first occurrence of a value
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print x # prints  ['to', 'or', 'not', 'to', 'be']

# reverse
x = [1, 2, 3]
x.reverse()
print x # prints [3, 2, 1]

#sort
x = [4, 6, 2, 1, 7, 9]
x.sort()
print x # prints [1, 2, 4, 6, 7, 9]

x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len) # sorted based on key, here it sorts based on len function of list
print x # prints ['add', 'acme', 'aerate', 'abalone', 'aardvark']

x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True) # sorts in reverse order
print x # prints [9, 7, 6, 4, 2, 1]

# only Tuple

# tuple function
print tuple('abc') # prints ('a', 'b', 'c')

