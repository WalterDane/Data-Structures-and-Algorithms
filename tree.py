from node import BinaryTreeNode
from queue import ListQueue

class BinaryTree(): #note, this the way this tree is built ensures a complete binary tree
    def __init__(self):
        self.root = None

    def insert(self, node):
        '''
        Insert from top to bottom, left to right. We will use level-order traversal BFT to achieve this
        '''
        self.level_order_insertion(node)

    def level_order_insertion(self, node):
        queue = ListQueue()

        if self.root == None:
            self.root = node
            queue.enqueue(self.root)
            print("Inserting root: " + str(self.root.data))
        else:
            item = queue.peek()
            if queue.is_empty() == False:
                if item.left_child == None:
                    item.left_child = node
                    queue.enqueue(item.left_child)
                    print("Inserting " +  str(item.left_child.data))
                else:
                    if item.right_child == None:
                        item.right_child = node
                        queue.enqueue(item.right_child)
                        print("Inserting " +  str(item.right_child.data))
                        queue.dequeue()
                        item = queue.peek()

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

    def in_order_traversal(self): #left, root, right
        """
        1. Recursively traverse the left subtree.
        2. Visit the root.
        3. Recursively traverse the right subtree.
        """
        pass

    def pre_order_traversal(self): #root, left, right
        """
        1. Visit the root
        2. Recursively traverse the left subtree
        3. Recursively traverse the right subtree
        """
        pass

    def post_order_traversal(self): #left, right, root
        """
        1. Recursively traverse the left subtree.
        2. Recursively traverse the right subtree.
        3. Visit the root.
        """
        pass

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
            
    def preorder_traversal(self): #TBI
        pass

    def inorder_traversal(self): #TBI
        pass

    def postorder_traversal(self): #TBI
        pass