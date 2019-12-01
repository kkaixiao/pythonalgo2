class DoublyLinkedListNode(object):

    def __init__(self, value):

        self.value = value
        self.next_node = None
        self.pre_node = None

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.next_node = b
b.pre_node = a

b.next_node = c
c.pre_node = b

print(b.pre_node.value)
print(b.next_node.value)
print(c.pre_node.value)
# print(a.pre_node.value)