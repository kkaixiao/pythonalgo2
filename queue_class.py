
class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enque(self, item):
        self.items.insert(0, item)

    def deque(self):
        self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
print(q.size())

print(q.isEmpty())

q.enque(1)
q.enque(2)
print(q.isEmpty())
print(q.size())

print(q.deque())

print(q.size())

q.deque()
print(q.size())

print(q.isEmpty())