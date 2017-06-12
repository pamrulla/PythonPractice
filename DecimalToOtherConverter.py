from Stack import Stack

def Converter(decimalNumber, base):
    letters = "0123456789ABCDEF"

    s = Stack()

    while decimalNumber > 0:
        s.push(decimalNumber % base)
        decimalNumber //= base

    convertedString = ""

    while not s.isEmpty():
        convertedString += letters[s.pop()]

    return convertedString

print Converter(25, 8)
print Converter(256, 16)
print Converter(26, 26)
