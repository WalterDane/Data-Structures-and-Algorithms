from node import BinaryTreeNode
from queue import ListQueue

class BinaryTree():
    def __init__(self):
        self.root = None
        self.queue = ListQueue()

    def insert(self, BinaryTreeNode):
        """
        Insert from top to bottom, left to right. We will use level-order traversal BFT to achieve this
        """
        self.level_order_insertion(BinaryTreeNode)

    def level_order_insertion(self, BinaryTreeNode):
        if self.root == None:
            self.root = BinaryTreeNode
            self.queue.enqueue(self.root)
            print("Inserting root: " + str(self.root.data))
        else:
            item = self.queue.peek()
            if self.queue.is_empty() == False:
                if item.left_child == None:
                    item.left_child = BinaryTreeNode
                    self.queue.enqueue(item.left_child)
                    print("Inserting " +  str(item.left_child.data))
                else:
                    if item.right_child == None:
                        item.right_child = BinaryTreeNode
                        self.queue.enqueue(item.right_child)
                        print("Inserting " +  str(item.right_child.data))
                        self.queue.dequeue()
                        item = self.queue.peek()

    def BFT(self):
        """
        Performs breadth first level order traversal on the tree
        Time Complexity: O(n)
        """
        self.queue = ListQueue()

        if self.root == None:
            print("Cannot perform breadth-first traversal because the tree is empty")
        else:
            self.queue.enqueue(self.root)
            item = self.queue.peek()
            print("Visiting root: " + str(item.data))
            while True:
                if self.queue.is_empty() == False:
                    if item.left_child != None:
                        self.queue.enqueue(item.left_child)
                        print("Visiting " +  str(item.left_child.data))
                    if item.right_child != None:
                        self.queue.enqueue(item.right_child)
                        print("Visiting " +  str(item.right_child.data))
                    self.queue.dequeue()
                    item = self.queue.peek()
                else:
                    print("All nodes have been visited!")
                    break

class BinarySearchTree(BinaryTree):
    def __init__(self): #TO BE IMPLEMENTED
        pass

nodes = []
node1 = BinaryTreeNode(1)
node2 = BinaryTreeNode(2)
node3 = BinaryTreeNode(3)
node4 = BinaryTreeNode(4)
node5 = BinaryTreeNode(5)
node6 = BinaryTreeNode(6)
node7 = BinaryTreeNode(7)
nodes.append(node1)
nodes.append(node2)
nodes.append(node3)
nodes.append(node4)
nodes.append(node5)
nodes.append(node6)
nodes.append(node7)
binary_tree = BinaryTree()
for node in nodes:
    binary_tree.insert(node)
binary_tree.BFT()