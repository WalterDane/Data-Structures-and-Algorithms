from node import Node

class Stack():
    def __init__(self):
        self.top = None

    def push(self, Node):
        if self.top == None:
            self.top = Node #genesis
        else:
            Node.next = self.top
            self.top = Node
        print("Pushing " + str(self.top.data))

    def pop(self):
        if self.top == None:
            print("Cannot perform pop operations because the stack is empty")
        else:
            print("Popping " + str(self.top.data))
            popped_node = self.top
            self.top = self.top.next
            del popped_node
            
    def peek(self):
        if self.top == None:
            print("Empty stack")
        else:
            print(self.top.data)
            return self.top.data

    def is_empty(self):
        if self.top == None:
            print("Stack is empty")