"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
"""

from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if len(self.q1) == 0:
            self.q1.appendleft(x)
            return

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1.appendleft(x)

        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0




class MyStack2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inbox = []
        self.buffer = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.inbox.append( x )


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len( self.inbox ) != 0:
            front_of_inbox = self.inbox.pop( 0 )

            if len( self.inbox ) != 0:
                self.buffer.append( front_of_inbox )
            else:
                top_element = front_of_inbox


        # swap inbox and buffer
        self.inbox, self.buffer = self.buffer, self.inbox

        return top_element



    def top(self) -> int:
        """
        Get the top element.
        """

        while len( self.inbox ) != 0:
            front_of_inbox = self.inbox.pop( 0 )

            if len( self.inbox ) != 0:
                self.buffer.append( front_of_inbox )
            else:
                self.buffer.append( front_of_inbox )
                top_element = front_of_inbox



        self.inbox, self.buffer = self.buffer, self.inbox

        return top_element


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.inbox) + len( self.buffer ) == 0:
            return True

        else:
            return False
