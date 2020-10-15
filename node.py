class BinaryTreeNode():
    def __init__(self, data = None):
        self.data = data
        self.left_child = None
        self.right_child = None

class TreeNode(): #n-ary tree node
    def __init__(self, data = None):
        self.data = data
        self.children = []

    def insert_child(self, node):
        self.children.append(node)

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None       