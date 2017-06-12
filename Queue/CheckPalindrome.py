from Deque import Deque

def CheckPalindrome(word): 
    q = Deque()

    for ch in word:
        q.addFront(ch)

    while q.size() > 1 and not q.isEmpty():
        if q.removeFront() != q.removeRear():
            return False
    return q.isEmpty() or q.size() == 1

print(CheckPalindrome("lsdkjfskf"))
print(CheckPalindrome("radar"))

