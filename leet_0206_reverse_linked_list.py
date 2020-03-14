class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse(head):

    current_node = head
    previous_node = None
    next_node = None

    while current_node:
        next_node = current_node.nextnode
        current_node.nextnode = previous_node

        previous_node = current_node
        current_node = next_node

    return previous_node





a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)


a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

reverse(a)

print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)
