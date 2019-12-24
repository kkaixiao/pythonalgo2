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


def pre_order(tree):
    if tree:
        print(tree.get_root_value())
        pre_order(tree.get_left_child())
        pre_order(tree.get_right_child())


def post_order(tree):
    if tree:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.get_root_value())


def in_order(tree):
    if tree:
        in_order(tree.get_left_child())
        print(tree.get_root_value())
        in_order(tree.get_right_child())


r = BinaryTree(3)
r.insert_left(4)

r.insert_right(6)
t = r.get_left_child()
t.insert_left(7)
t.insert_right(8)

# pre_order(r)
# post_order(r)
in_order(r)