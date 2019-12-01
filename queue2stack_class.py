class Queue2Stacks(object):

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def deque(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()

q = Queue2Stacks()

q.enqueue('hello')
q.enqueue('crazy')
q.enqueue('world')

print(q.deque())

print(q.deque())

print(q.deque())