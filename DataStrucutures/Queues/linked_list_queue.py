class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.num_elements = 0
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.num_elements == 0:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

        self.num_elements += 1
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0
    
    def dequeue(self):
        if self.num_elements == 0:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            self.num_elements -= 1
            return value

    
    