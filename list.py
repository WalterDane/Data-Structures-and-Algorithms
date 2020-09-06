from node import Node

class List():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, node):
        """
        Inserts a node to the end of the list.
        Time Complexity: Since a tail pointer is kept, the insert operation is O(1)
        """
        if self.head == None:
            self.head = node #genesis node
        else:
            if self.head.next == None and self.tail == None:
                self.head.next = node #sneaky
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node

    def index_helper(self, value, previous_node, node):
        if node.data == value:
            if node == self.head:
                node_reference = [node]
                return node_reference
            else:
                node_references = [previous_node, node]
                return node_references
        else:
            previous_node = node #current node now becomes the previous node
            nodes = self.index_helper(value, previous_node, node.next) #sneaky
            return nodes

    def index(self, value, head):
        """
        Traverses the list until the desired value is found.
        Time Complexity: O(n)
        """
        node_references = self.index_helper(value, None, self.head)
        return node_references

    def traverse_helper(self, node):
        if node.next == None:
            print(node.data)
        else:
            print(node.data)
            self.traverse_helper(node.next)

    def traverse(self, head):
        self.traverse_helper(head)

    def delete(self, value):
        """
        Deletes the node with the specified value.
        Time Complexity: O(1) if we do not consider indexing time
        """
        node_references = self.index(value, self.head)
        if len(node_references) == 1: #head
            head = node_references[0]
            self.head = head.next
            del head
        else:
            previous_node = node_references[0]
            current_node = node_references[1]
            if current_node.next == None: #tail
                self.tail = previous_node
                self.tail.next = None
                del current_node
            else: #middle
                previous_node.next = current_node.next
                del current_node

rapper1 = "Trippie Redd"
rapper2 = "Metro Boomin"
rapper3 = "Young Metro Boomin"
rapper4 = "PartyNextDoor"
rapper5 = "Little Uzi Vert"
node1 = Node(rapper1)
node2 = Node(rapper2)
node3 = Node(rapper3)
node4 = Node(rapper4)
node5 = Node(rapper5)

linked_list = List()
linked_list.insert(node1)
linked_list.insert(node2)
linked_list.insert(node3)
linked_list.insert(node4)
linked_list.insert(node5)
linked_list.delete("Young Metro Boomin")
linked_list.traverse(linked_list.head)