class BinaryTree(object):
    def __init__(self, root_obj):
        self.key = root_obj
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left = self.left
            self.left = t

    def insert_right(self, new_node):
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right = self.right
            self.right = t

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def set_root_val(self, obj):
        self.key = obj

    def get_root_value(self):
        return self.key


r = BinaryTree(3)
r.insert_left(4)

print(r.key)
print(r.left.key)
r.insert_right('5fff')
a = r.get_right_child()
print(a.get_root_value())