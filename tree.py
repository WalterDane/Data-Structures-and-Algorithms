from node import BinaryTreeNode
from myqueues import ListQueue

class BinaryTree(): #note, this the way this tree is built ensures a complete binary tree
    def __init__(self):
        self.root = None
        self.queue = ListQueue()

    def insert(self, node):
        '''
        Insert from top to bottom, left to right. We will use level-order traversal BFT to achieve this
        '''
        self.level_order_insertion(node)

    def level_order_insertion(self, node):
        if self.root == None:
            self.root = node
            self.queue.enqueue(self.root)
            print("Inserting " + str(self.root.data))
        else:
            item = self.queue.peek()
            if self.queue.is_empty() == False:
                if item.left_child == None:
                    item.left_child = node
                    self.queue.enqueue(item.left_child)
                    print("Inserting " +  str(item.left_child.data))
                else:
                    if item.right_child == None:
                        item.right_child = node
                        self.queue.enqueue(item.right_child)
                        print("Inserting " +  str(item.right_child.data))
                        self.queue.dequeue()
                        item = self.queue.peek()

    def level_order_traversal(self):
        '''
        Performs breadth first level order traversal on the tree
        Time Complexity: O(n)
        '''
        queue = ListQueue()

        if self.root == None:
            print("Cannot perform breadth-first traversal because the tree is empty")
        else:
            queue.enqueue(self.root)
            item = queue.peek()
            print("Visiting root: " + str(item.data))
            while True:
                if queue.is_empty() == False:
                    if item.left_child != None:
                        queue.enqueue(item.left_child)
                        print("Visiting " +  str(item.left_child.data))
                    if item.right_child != None:
                        queue.enqueue(item.right_child)
                        print("Visiting " +  str(item.right_child.data))
                    queue.dequeue()
                    item = queue.peek()
                else:
                    print("All nodes have been visited!")
                    break
    
    def cannot_traverse(self):
        print("Cannot traverse because the tree is empty")

    def in_order_traversal_helper(self, node):
        if node == None:
            return
        else:
            self.in_order_traversal_helper(node.left_child)
            print(node.data)
            self.in_order_traversal_helper(node.right_child)
            
    def in_order_traversal(self): #left, root, right
        """
        1. Recursively traverse the left subtree.
        2. Visit the root.
        3. Recursively traverse the right subtree.
        """
        if self.root == None:
            self.cannot_traverse()
        else:
            self.in_order_traversal_helper(self.root)

    def pre_order_traversal_helper(self, node):
        if node == None:
            return
        else:
            print(node.data)
            self.pre_order_traversal_helper(node.left_child)
            self.pre_order_traversal_helper(node.right_child)

    def pre_order_traversal(self): #root, left, right
        """
        1. Visit the root.
        2. Recursively traverse the left subtree.
        3. Recursively traverse the right subtree.
        """
        if self.root == None:
            self.cannot_traverse()
        else:
            self.pre_order_traversal_helper(self.root)
    
    def post_order_traversal_helper(self, node):
        if node == None:
            return
        else:
            self.post_order_traversal_helper(node.left_child)
            self.post_order_traversal_helper(node.right_child)
            print(node.data)

    def post_order_traversal(self): #left, right, root
        """
        1. Recursively traverse the left subtree.
        2. Recursively traverse the right subtree.
        3. Visit the root.
        """
        if self.root == None:
            self.cannot_traverse()
        else:
            self.post_order_traversal_helper(self.root)

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert_helper(self, parent, node):
        if node.data < parent.data:
            if parent.left_child == None:
                parent.left_child = node
                print("Inserting left child: " + str(parent.left_child.data) + " under parent: " + str(parent.data))
            else:
                self.insert(parent.left_child, node)
        if node.data >= parent.data:
            if parent.right_child == None:
                parent.right_child = node
                print("Inserting right child: " + str(parent.right_child.data) + " under parent: " + str(parent.data))
            else:
                self.insert_helper(parent.right_child, node)

    def insert(self, node):
        """
        Inserts the node into the Binary Search Tree. The root node
        will be passed first.
        Time Complexity: O(n)
        """
        if self.root == None:
            self.root = node
            self.parent = self.root
        else:
            self.insert_helper(self.root, node)