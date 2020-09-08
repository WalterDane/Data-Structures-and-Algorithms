from node import Node

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, Node):
        if self.front == None:
            self.front = Node
            print("Inserting: " + str(self.front.data))
        else:
            if self.front.next == None:
                self.front.next = Node
                self.rear = Node
                print("Inserting: " + str(self.rear.data))
            else:
                self.rear.next = Node
                self.rear = Node
                print("Inserting: " + str(self.rear.data))
            
    def dequeue(self):
        if self.front == None:
            print("Can't dequeue because queue is empty")
        else:
            print("Dequeuing " + str(self.front.data))
            self.front = self.front.next #garbabe collector will clean up old object since there's no reference to it
    
    def peek(self):
        print(self.front.data)
        return self.front.data