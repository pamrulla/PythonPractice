def hello(name):
    return 'Hello, ' + name + '!'

print hello('world')
print hello('Gumby')

def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result

print fibs(10)
print fibs(15)

def try_to_change(n):
    n = 'Mr. Gumby'
name = 'Mrs. Entity'
try_to_change(name)
print name #'Mrs. Entity'

def change(n):
    n[0] = 'Mr. Gumby'
names = ['Mrs. Entity', 'Mrs. Thing']
change(names)
print names #['Mr. Gumby', 'Mrs. Thing']

def print_params_4(x, y, z=3, *pospar, **keypar):
    print x, y, z
    print pospar
    print keypar

print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
# 1 2 3
# (5, 6, 7)
# {'foo': 1, 'bar': 2}

print_params_4(1, 2)
# 1 2 3
# ()
# {}

def story(**kwds):
    return 'Once Upon a time, there was a ' \
            '%(job)s called %(name)s. ' % kwds;

def power(x, y, *others):
    if others:
        print 'Received redundant parameters:', others
    return pow(x, y)

def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None: # If the stop is not supplied...
        start, stop = 0, start # shuffle the parameters
    result = []
    i = start # We start counting at the start index
    while i < stop: # Until the index reaches the stop index...
        result.append(i) # ...append the index to the result...
        i += step # ...increment the index with the step (> 0)
    return result

print story(job='king', name='Gumby') # Once upon a time, there was a king called Gumby.

print story(name='Sir Robin', job='brave knight') # Once upon a time, there was a brave knight called Sir Robin.

params = {'job': 'language', 'name': 'Python'}
print story(**params) # Once upon a time, there was a language called Python.

del params['job']
print story(job='stroke of genius', **params) # Once upon a time, there was a stroke of genius called Python.

print power(2,3) # 8

print power(3,2) # 9

print power(y=3,x=2) # 8

params = (5,) * 2

print power(*params) # 3125

print power(3, 3, 'Hello, world') # Received redundant parameters: Hello, world
                                  # 27

print interval(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print interval(1,5) # [1, 2, 3, 4]

print interval(3,12,4) # [3, 7, 11]

print power(*interval(3,7)) # Received redundant parameters: (5, 6)
                            # 81

# Accesing gloval scope variables
x = 1
def change_global():
    global x
    x = x + 1
change_global()
print x # 2


# Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print factorial(4)
