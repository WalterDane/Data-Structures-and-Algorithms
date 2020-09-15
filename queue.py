from node import Node
from node import BinaryTreeNode

class LinkedListQueue():
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, Node):
        """
        Prepends node to the beginning of the list
        Time Complexity: O(1)
        """
        if self.front == None:
            self.front = Node
            #print("Inserting: " + str(self.front.data))
        else:
            if self.front.next == None:
                self.front.next = Node
                self.rear = Node
                #print("Inserting: " + str(self.rear.data))
            else:
                self.rear.next = Node
                self.rear = Node
                #print("Inserting: " + str(self.rear.data))
            
    def dequeue(self):
        """
        Removes node at the end of the list
        Time Complexity: O(1)
        """
        if self.front == None:
            print("Can't dequeue because queue is empty")
        else:
            #print("Dequeuing " + str(self.front.data))
            self.front = self.front.next #garbabe collector will clean up old object since there's no reference to it
    
    def peek(self):
        print(self.front.data)
        return self.front.data
    
    def is_empty(self):
        if self.front == None:
            print("Stack is empty")
            return True
        else:
            return False

class ListQueue():
    def __init__(self):
        self.queue = []

    def enqueue(self, Node):
        """
        Prepends node to the beginning of the list
        Time Complexity: O(n)
        """
        self.queue.append(Node)

    def dequeue(self):
        """
        Removes node at the end of the list
        Time Complexity: O(1)
        """
        self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            return self.queue[0]

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def print_queue(self):
        print(self.queue)