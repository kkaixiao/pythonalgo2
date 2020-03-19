
"""
mplement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.main.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        temp = []
        while len(self.main) > 0:
            top = self.main.pop()
            temp.append(top)
        result = temp.pop()
        while len(temp) > 0:
            top = temp.pop()
            self.main.append(top)
        return result

    def peek(self) -> int:
        """
        Get the front element.
        """
        temp = []
        while len(self.main) > 0:
            top = self.main.pop()
            temp.append(top)
        result = temp[-1]
        while len(temp) > 0:
            top = temp.pop()
            self.main.append(top)
        return result

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.main) == 0