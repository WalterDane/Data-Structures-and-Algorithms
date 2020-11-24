from node import Node
from node import BinaryTreeNode

class LinkedListQueue():
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, Node):
        if self.front == None:
            self.front = Node
        else:
            if self.front.next == None:
                self.front.next = Node
                self.rear = Node
            else:
                self.rear.next = Node
                self.rear = Node
            
    def dequeue(self):
        if self.front == None:
            print("Can't dequeue because queue is empty")
        else:
            self.front = self.front.next
    
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
        self.queue.append(Node)

    def dequeue(self):
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

class PriorityQueue:
    def __init__(self):
        self.priority_queue = []

    def enqueue(self, value):
        self.priority_queue.append(value)
        self.priority_queue = sorted(self.priority_queue, reverse=True)

    def dequeue(self):
        return self.priority_queue.pop()

    def is_empty(self):
        if len(self.priority_queue) == 0:
            print("priority queue is empty")