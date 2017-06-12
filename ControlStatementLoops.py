# Below are false.
# False None 0 "" () [] {}
print False == True
print None == True
print 0 == True
print () == True
print "" == True
print [] == True
print {} == True

# if-else
name = raw_input('What is your name? ')
if name.endswith('Gumby'):
    print 'Hello, Mr. Gumby'
else:
    print 'Hello, stranger'

#elif
num = input('Enter a number: ')
if num > 0:
    print 'The number is positive'
elif num < 0:
    print 'The number is negative'
else:
    print 'The number is zero'

# nested
name = raw_input('What is your name? ')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print 'Hello, Mr. Gumby'
    elif name.startswith('Mrs.'):
        print 'Hello, Mrs. Gumby'
    else:
        print 'Hello, Gumby'
else:
    print 'Hello, stranger'

# Expression        Description
# x == y            x equals y.
# x < y             x is less than y.
# x > y             x is greater than y.
# x >= y            x is greater than or equal to y.
# x <= y            x is less than or equal to y.
# x != y            x is not equal to y.
# x is y            x and y are the same object.
# x is not y        x and y are different objects.
# x in y            x is a member of the container (e.g., sequence) y.
# x not in y        x is not a member of the container (e.g., sequence) y.

# Loops

# while
x = 1
while x <= 100:
    print x
x += 1

# for
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print word

for number in range(1,101):
    print number

d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print key, 'corresponds to', d[key]

for key, value in d.items():
    print key, 'corresponds to', value

# Parallel Iteration - iterating two lists at a time.
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for name, age in zip(names, ages):
    print name, 'is', age, 'years old'

# break
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print n
    break

# continue
# for x in seq:
#   if condition1: continue
#   if condition2: continue
#   if condition3: continue
#   do_something()
#   do_something_else()
#   do_another_thing()
#   etc()

# pass - nothing executes

# exec The statement for executing a string is exec
exec "print 'Hello, world!'" # Hello, world!

# eval - executes python expressions
eval(raw_input("Enter an arithmetic expression: "))
# Enter an arithmetic expression: 6 + 18 * 2
# 42





