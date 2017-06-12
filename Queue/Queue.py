class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self, item):
        return self.items.pop()

    def isEmpty(self):
        return self.items.count == 0

    def size(self):
        return self.items.count
