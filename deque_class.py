class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d = Deque()
print(d.isEmpty())

d.addFront('Hello')
d.addRear('World')

print(d.isEmpty())

print(d.size())

print(d.removeFront() + ' ' + d.removeRear())

print(d.isEmpty())