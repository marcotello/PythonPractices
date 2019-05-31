'''
Linked List Practice
Implement a linked list class. Your class should be able to:

Append data to the tail of the list and prepend to the head
Search the linked list for a value and return the node
Remove a node
Pop, which means to return the first node's value and delete the node from the list
Insert data at some position in the list
Return the size (length) of the linked list
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        if self.head:
            temp_node = self.head
            self.head = Node(value)
            self.head.next = temp_node
            return
        else:
            self.head = Node(value)
            return

    
    def append(self, value):
        """ Append a value to the end of the list. """
        if self.head:
            current = self.head
            
            while current.next:
                current = current.next

            current.next = Node(value)
        else:
            self.prepend(value)
    
    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        current =  self.head
        while current:
            if current.value == value:
                return current
            
            current = current.next
        
        return None
        
    
    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head:
            current =  self.head

            if current.value == value:
                self.head = current.next
            else:
                while current.next:
                    if current.next.value == value:
                        current.next = current.next.next
                        break
                    else:
                        current = current.next

    
    def pop(self):
        """ Return the first node's value and remove it from the list. """
        current =  self.head
        if current.next:
            self.head = current.next
            return current.value
        else:
            self.head = None
            return self.head
    
    def size(self):
        """ Return the size or length of the linked list. """
        index = 0
        if self.head:
            current = self.head
            while current:
                index += 1
                current = current.next

        return index
    
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos > self.size():
            self.append(value)
        else:
            if self.head:
                index = 1
                current = self.head

                if pos < 1:
                    self.head = Node(value)
                    self.head.next = current
                else:
                    while current:
                        if index == pos:
                            temp_node = current.next
                            current.next = Node(value)
                            current.next.next = temp_node
                        
                        index += 1
                        current = current.next

            else:
                self.prepend(value)
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

##############################

## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
print("assert 1 passed")
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
print("assert 2 passed")
    
# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
print("assert 3 passed")
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"
print("assert 4 passed")

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
print("assert 7 passed")
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
print("assert 8 passed")
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"
print("assert 9 passed")

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
print("assert 10 passed")
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"
print("assert 11 passed")

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
print("assert 12 passed")
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
print("assert 13 passed")
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
print("assert 14 passed")

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"
print("asser 15 passed")