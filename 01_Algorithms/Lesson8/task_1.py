from binarytree import tree, bst, Node


class MyNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


a = tree(height=4, is_perfect=False)
print(a)
b = bst(height=3, is_perfect=True)
print(b)


def func():
    pass

root = MyNode(25)
root.left = MyNode(func)
root.right = MyNode(36)
root.left.left = MyNode(7)

print(root)

