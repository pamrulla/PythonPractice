# Strins are immutable
# Formatting
format = "Hello, %s. %s enough for ya?"
values = ("world", "hot") # Only tuples and dictionaries are considered as multiple values
print format % values # prints Hello, world. hot enough for ya?
listValues = ["world", "hot"]
# print format % listValues # thorws exception, as list is considered as one value so format string needs two values.

format = "Pi with three decimals: %.3f"
from math import pi
print format % pi # pints Pi with three decimas: 3.142

print 'Price of eggs: $%d' % 42 # 'Price of eggs: $42'
print 'Hexadecimal price of eggs: %x' % 42 # 'Hexadecimal price of eggs: 2a'
from math import pi
print 'Pi: %f...' % pi # 'Pi: 3.141593...'
print 'Very inexact estimate of pi: %i' % pi #'Very inexact estimate of pi: 3'
print 'Using str: %s' % 42L # 'Using str: 42'
print 'Using repr: %r' % 42L # 'Using repr: 42L'

print '%10f' % pi # '  3.141593'
print '%10.2f' % pi # '      3.14'
print '%.5s' % 'Guido van Rossum' # 'Guido'
print '%.*s' % (5, 'Guido van Rossum') # 'Guido'

print '%010.2f' % pi # '0000003.14'
print '%-10.2f' % pi # '3.14      ' left align
print ('%+5d' % 10) + '\n' + ('%+5d' % -10) # +10
                                            # -10

# Write a program to print a formatted price list with a given width
# Please enter width: 35
# ===================================
# Item                          Price
# �����������������������������������
# Apples                         0.40
# Pears                          0.50
# Cantaloupes                    1.92
# Dried Apricots (16 oz.)        8.00
# Prunes (4 lbs.)               12.00
# ===================================

# find
title = "Monty Python's Flying Circus"
title.find('Monty') # 0
title.find('Python') # 6
title.find('Zirquss') # -1

subject = '$$$ Get rich now!!! $$$'
subject.find('$$$', 1) # Only supplying the start
subject.find('!!!', 0, 16) # Supplying start and end

# join
seq = ['1', '2', '3', '4', '5']
sep = '+'
print sep.join(seq) # '1+2+3+4+5'
dirs = '', 'usr', 'bin', 'env'
print '/'.join(dirs) # '/usr/bin/env'

# lower
name = 'Gumby'
print name.lower()

# replace
print 'This is a test'.replace('is', 'eez') # 'Theez eez a test'

# split
print '1+2+3+4+5'.split('+') # ['1', '2', '3', '4', '5']

# strip
print '     internal whitespace is kept      '.strip() # 'internal whitespace is kept'

