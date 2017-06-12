phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'} # key:value key should be unique

# dict()
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print d # {'age': 42, 'name': 'Gumby'}

d = dict(name='Gumby', age=42)
print d # {'age': 42, 'name': 'Gumby'}

# len()
print len(d) # 2

print d['name'] # Gumby

del d['name']
print d # {'age': 42}

d['name'] = 'Khan'
print d # {'age': 42, 'name': 'Khan'}

print 'name' in d # True
print 'gender' in d # False

# Write a program to mimic telephone dictionary.
# Name: Beth
# Phone number (p) or address (a)? p
# Beth's phone number is 9102.

# clear()
d.clear()
print d # {}

# copy() - Shallow copy - have same reference.
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print y # {'username': 'mlh', 'machines': ['foo', 'baz']}
print x # {'username': 'mlh', 'machines': ['foo', 'baz']}

from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print c # {'names': ['Alfred', 'Bertrand', 'Clive']}
print dc # {'names': ['Alfred', 'Bertrand']}

# fromKeys() - creates dictionary with only keys.
print dict.fromkeys(['name', 'age']) # {'age': None, 'name': None}
print dict.fromkeys(['name', 'age'], '(unknown)') # {'age': '(unknown)', 'name': '(unknown)'}

# get()
print d.get('name') # None
print d.get('name', 'N/A') # N/A

# has_key()
d = {}
print d.has_key('name') # False
d['name'] = 'Eric'
print d.has_key('name') # True

# items and iteritems
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print d.items() # [('url', 'http://www.python.org'), ('spam', 0), ('title', 'Python Web Site')]

it = d.iteritems()
print it # <dictionary-iterator object at 169050>
print list(it)  # Convert the iterator to a list
                # [('url', 'http://www.python.org'), ('spam', 0), ('title', 'Python Web Site')]

# keys and iterkeys - The keys method returns a list of the keys in the dictionary, while iterkeys returns an iterator over the keys.
# values and itervalues - The values method returns a list of the values in the dictionary (and itervalues returns an iterator of the values).

# pop()
d = {'x': 1, 'y': 2}
d.pop('x') # 1
print d # {'y': 2}

# popitem() - removes arbitraru item
d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
print d.popitem() # ('url', 'http://www.python.org')
print d # {'spam': 0, 'title': 'Python Web Site'}

# setdefault() - returns default value if key is not present and updates dictionary with defualt value provided
d = {}
print d.setdefault('name', 'N/A') # 'N/A'
print d # {'name': 'N/A'}
d['name'] = 'Gumby'
print d.setdefault('name', 'N/A') # 'Gumby'
print d # {'name': 'Gumby'}

# update()
d = {
'title': 'Python Web Site',
'url': 'http://www.python.org',
'changed': 'Mar 14 22:09:15 MET 2008'
}
x = {'title': 'Python Language Website'}
d.update(x)
print d  # {'url': 'http://www.python.org', 'changed': 'Mar 14 22:09:15 MET 2008', 'title': 'Python Language Website'}
