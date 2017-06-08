""" To check the paranthesis are balanced or not """
from Stack import Stack

def parChecker(expression):
    s = Stack()
    opens = "([{"
    closes = ")]}"
    for c in expression:
        if c in opens:
            s.push(c)
        elif c in closes:
            if s.isEmpty():
                return False
            if closes.index(c) == opens.index(s.peek()) :
                s.pop()
            else:
                return False
    return s.isEmpty()

print parChecker('((()))')
print parChecker('((())')
print parChecker('()))')
print parChecker('( [ ) ]')
print parChecker('( ( ( ) ] ) )')
print parChecker('[ { ( ) ]')
print parChecker('{ { ( [ ] [ ] ) } ( ) }')
print parChecker('[ [ { { ( ( ) ) } } ] ]')
print parChecker('[ ] [ ] [ ] ( ) { }')
